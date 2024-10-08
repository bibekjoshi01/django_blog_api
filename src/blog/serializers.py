from typing import Any
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model

from src.base.serializers import AbstractInfoRetrieveSerializer
from src.blog.validators import validate_blog_media
from src.libs.get_context import get_user_by_context
from src.blog.models import PostCategory, PostTag, Post

User = get_user_model()

# Blog Post Category Serializers


class PostCategoryListSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = PostCategory
        fields = ["id", "name", "description", "slug", "post_count", "sub_categories"]

    def get_post_count(self, obj) -> int:
        return obj.get_post_count()

    def get_sub_categories(self, obj):
        if obj.is_leaf_node():
            return None
        serializer = self.__class__(obj.get_children(), many=True)
        return serializer.data


class PostCategoryDetailSerializer(AbstractInfoRetrieveSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta(AbstractInfoRetrieveSerializer.Meta):
        model = PostCategory
        fields = ["id", "name", "description", "parent", "slug", "post_count"]

        fields += AbstractInfoRetrieveSerializer.Meta.fields

    def get_post_count(self, obj) -> int:
        return obj.get_post_count()


class PostCategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = ["name", "slug", "description", "parent"]

    def validate_name(self, name):
        """
        Validate that the name is unique.
        """
        if PostCategory.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                f"A category with the name '{name}' already exists."
            )
        return name

    def create(self, validated_data):
        created_by = get_user_by_context(self.context)

        return PostCategory.objects.create(
            created_by=created_by,
            **validated_data,
        )

    def to_representation(self, instance):
        return {
            "type": "Created",
            "message": "Category Created Successfully.",
            "id": instance.id,
        }


class PostCategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = ["name", "description", "is_active"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def to_representation(self, instance):
        return {
            "type": "Updated",
            "message": "Category Updated Successfully.",
            "id": instance.id,
        }


# Blog Post Tag Serializers


class PostTagListSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = PostTag
        fields = ["id", "name", "description", "slug", "post_count"]

    def get_post_count(self, obj) -> int:
        return obj.get_post_count()


class PostTagDetailSerializer(AbstractInfoRetrieveSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta(AbstractInfoRetrieveSerializer.Meta):
        model = PostTag
        fields = ["id", "name", "description", "slug", "post_count"]

        fields += AbstractInfoRetrieveSerializer.Meta.fields

    def get_post_count(self, obj) -> int:
        return obj.get_post_count()


class PostTagCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostTag
        fields = ["name", "slug", "description"]

    def validate_name(self, name):
        """
        Validate that the name is unique.
        """
        if PostTag.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                f"A Tag with the name '{name}' already exists."
            )
        return name

    def create(self, validated_data):
        created_by = get_user_by_context(self.context)

        return PostTag.objects.create(
            created_by=created_by,
            **validated_data,
        )

    def to_representation(self, instance):
        return {
            "type": "Created",
            "message": "Tag Created Successfully.",
            "id": instance.id,
        }


class PostTagUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostTag
        fields = ["name", "description", "is_active"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def to_representation(self, instance):
        return {
            "type": "Updated",
            "message": "Tag Updated Successfully.",
            "id": instance.id,
        }


# Blog Post Serializers


class PostListSerializer(serializers.ModelSerializer):
    total_comments = serializers.SerializerMethodField()
    unread_comments = serializers.SerializerMethodField()
    author_full_name = serializers.ReadOnlyField(source="get_author_full_name")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "categories",
            "tags",
            "author_full_name",
            "unread_comments",
            "total_comments",
        ]

    def get_unread_comments(self, obj) -> int:
        return obj.comments.filter(is_seen=False, is_archived=False).count()

    def get_total_comments(self, obj) -> int:
        return obj.comments.filter(is_archived=False).count()

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.status == "PUBLISHED":
            data["published_at"] = instance.published_at
        else:
            data["updated_at"] = instance.updated_at

        return data


class CategorySerializerForPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ["id", "name"]


class TagSerializerForPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ["id", "name"]


class PostDetailSerializer(serializers.ModelSerializer):
    author_full_name = serializers.ReadOnlyField(source="get_author_full_name")
    categories = CategorySerializerForPostDetailSerializer(many=True)
    tags = TagSerializerForPostDetailSerializer(many=True)
    
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "status",
            "views",
            "up_votes",
            "down_votes",
            "categories",
            "tags",
            "published_at",
            "author_full_name",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.status == "PUBLISHED":
            data["published_at"] = instance.published_at
        else:
            data["updated_at"] = instance.updated_at

        return data


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_archived=False, is_active=True)
    )
    categories = serializers.PrimaryKeyRelatedField(
        queryset=PostCategory.objects.filter(is_archived=False, is_active=True),
        many=True,
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=PostTag.objects.filter(is_archived=False, is_active=True), many=True
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "status",
            "format",
            "visibility",
            "content",
            "excerpt",
            "author",
            "read_time",
            "categories",
            "tags",
            "stick_at_top",
            "allow_comments",
        ]

    def validate(self, attrs) -> Any:
        return super().validate(attrs)

    def validate_slug(self, slug):
        if Post.objects.filter(slug=slug).exists():
            raise serializers.ValidationError("Post with slug already exists.")
        return slug

    def create(self, validated_data) -> Any:
        created_by = get_user_by_context(self.context)
    
        categories = validated_data.pop("categories", [])
        tags = validated_data.pop("tags", [])

        if validated_data["status"] == "PUBLISEHD":
            validated_data["published_at"] = timezone.now()

        post = Post.objects.create(
            title=validated_data.pop("title").title(),
            slug=validated_data.pop("slug"),
            created_by=created_by,
            **validated_data,
        )

        for category in categories:
            post.categories.add(category)

        for tag in tags:
            post.tags.add(tag)

        return post


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "content", "is_active"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def to_representation(self, instance):
        return {
            "type": "Updated",
            "message": "Post Updated Successfully.",
            "id": instance.id,
        }
