# Generated by Django 5.1.4 on 2024-12-17 08:41

import uuid

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Represents unique uuid.",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this object should be treated as active. Unselect this instead of deleting instances.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this object should be treated as delected. Unselect this instead of deleting instances.",
                        verbose_name="archived",
                    ),
                ),
                (
                    "email_type",
                    models.CharField(
                        choices=[
                            ("INFO", "Info"),
                            ("SALES", "Sales"),
                            ("SUPPORT", "Support"),
                        ],
                        default="INFO",
                        help_text="Type of email (e.g. sales, info)",
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "email_host",
                    models.CharField(
                        default="smtp.gmail.com",
                        help_text="SMTP server address",
                        max_length=255,
                    ),
                ),
                (
                    "email_use_tls",
                    models.BooleanField(
                        default=True, help_text="Use TLS for the email connection"
                    ),
                ),
                (
                    "email_use_ssl",
                    models.BooleanField(
                        default=False, help_text="Use SSL for the email connection"
                    ),
                ),
                (
                    "email_port",
                    models.PositiveIntegerField(
                        default=587, help_text="Port for the email server"
                    ),
                ),
                (
                    "email_host_user",
                    models.EmailField(help_text="Email host user", max_length=254),
                ),
                (
                    "email_host_password",
                    models.CharField(help_text="Email host password", max_length=255),
                ),
                (
                    "default_from_email",
                    models.EmailField(
                        help_text="Default 'from' email address", max_length=254
                    ),
                ),
                (
                    "server_mail",
                    models.EmailField(
                        blank=True,
                        help_text="Email address for server errors",
                        max_length=254,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Email Configuration",
                "verbose_name_plural": "Email Configurations",
            },
        ),
        migrations.CreateModel(
            name="OrganizationSetup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Represents unique uuid.",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this object should be treated as active. Unselect this instead of deleting instances.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this object should be treated as delected. Unselect this instead of deleting instances.",
                        verbose_name="archived",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the organization",
                        max_length=255,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        help_text="Display name of the organization",
                        max_length=255,
                        verbose_name="Display Name",
                    ),
                ),
                (
                    "favicon",
                    models.ImageField(
                        help_text="Favicon of the organization",
                        max_length=255,
                        null=True,
                        upload_to="organization_setup",
                        verbose_name="Favicon",
                    ),
                ),
                (
                    "tagline",
                    models.CharField(
                        blank=True,
                        help_text="Tagline of the organization",
                        max_length=255,
                        verbose_name="Tagline",
                    ),
                ),
                (
                    "logo_main",
                    models.ImageField(
                        help_text="Main logo of the organization",
                        max_length=255,
                        null=True,
                        upload_to="organization_setup",
                        verbose_name="Main Logo",
                    ),
                ),
                (
                    "logo_alt",
                    models.ImageField(
                        help_text="Alternate logo of the organization",
                        null=True,
                        upload_to="organization_setup",
                        verbose_name="Alternate Logo",
                    ),
                ),
                (
                    "website_url",
                    models.URLField(
                        blank=True,
                        help_text="URL of the organization's website",
                        verbose_name="Website URL",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        help_text="Address of the organization",
                        max_length=255,
                        verbose_name="Address",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Email of the organization",
                        max_length=254,
                        verbose_name="Email",
                    ),
                ),
                (
                    "privacy_policy_en",
                    models.TextField(
                        help_text="Privacy Policy of the organization (english)",
                        verbose_name="Privacy Policy English",
                    ),
                ),
                (
                    "privacy_policy_fr",
                    models.TextField(
                        help_text="Privacy Policy of the organization (french)",
                        verbose_name="Privacy Policy French",
                    ),
                ),
                (
                    "cookie_policy_en",
                    models.TextField(
                        help_text="Cookie Policy of the organization (english)",
                        verbose_name="Cookie Policy English",
                    ),
                ),
                (
                    "cookie_policy_fr",
                    models.TextField(
                        help_text="Cookie Policy of the organization (french)",
                        verbose_name="Cookie Policy French",
                    ),
                ),
                (
                    "policies_en",
                    models.TextField(
                        blank=True,
                        help_text="Policies of the organization (english)",
                        verbose_name="Policies English",
                    ),
                ),
                (
                    "policies_fr",
                    models.TextField(
                        blank=True,
                        help_text="Policies of the organization (french)",
                        verbose_name="Policies French",
                    ),
                ),
                (
                    "about_us_en",
                    models.TextField(
                        blank=True,
                        help_text="Context for the about us page (english)",
                        verbose_name="About Us English",
                    ),
                ),
                (
                    "about_us_fr",
                    models.TextField(
                        blank=True,
                        help_text="Context for the about us page (french)",
                        verbose_name="About Us French",
                    ),
                ),
                (
                    "terms_of_use_en",
                    models.TextField(blank=True, verbose_name="Terms of Use (English)"),
                ),
                (
                    "terms_of_use_fr",
                    models.TextField(blank=True, verbose_name="Terms of Use (French)"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization Detail",
                "verbose_name_plural": "Organization Details",
            },
        ),
        migrations.CreateModel(
            name="OrganizationDonationLinks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Represents unique uuid.",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this object should be treated as active. Unselect this instead of deleting instances.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this object should be treated as delected. Unselect this instead of deleting instances.",
                        verbose_name="archived",
                    ),
                ),
                (
                    "payment_gateway",
                    models.CharField(
                        choices=[
                            ("PAYPAL", "PayPal"),
                            ("STRIPE", "Stripe"),
                            ("FLUTTERWAVE", "Flutterwave"),
                        ],
                        max_length=20,
                    ),
                ),
                ("link", models.URLField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donation_links",
                        to="core.organizationsetup",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationSocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Represents unique uuid.",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this object should be treated as active. Unselect this instead of deleting instances.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this object should be treated as delected. Unselect this instead of deleting instances.",
                        verbose_name="archived",
                    ),
                ),
                (
                    "social_media",
                    models.CharField(
                        choices=[
                            ("FACEBOOK", "Facebook"),
                            ("TWITTER", "Twitter"),
                            ("YOUTUBE", "Youtube"),
                            ("INSTAGRAM", "Instagram"),
                            ("WHATS-APP", "Whats-app"),
                        ],
                        max_length=20,
                    ),
                ),
                ("link", models.URLField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_media_links",
                        to="core.organizationsetup",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ThirdPartyCredential",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Represents unique uuid.",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this object should be treated as active. Unselect this instead of deleting instances.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_archived",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this object should be treated as delected. Unselect this instead of deleting instances.",
                        verbose_name="archived",
                    ),
                ),
                (
                    "gateway",
                    models.CharField(
                        choices=[
                            ("GOOGLE", "Google"),
                            ("PAYPAL", "Paypal"),
                            ("STRIPE", "Stripe"),
                            ("FLUTTERWAVE", "Flutterwave"),
                            ("EXCHANGE-RATE", "Exchange Rate API"),
                        ],
                        help_text="Select the payment gateway from the list (e.g., Google, Paypal).",
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "base_url",
                    models.URLField(
                        blank=True,
                        help_text="Base URL for the payment gateway's API (e.g., https://api.paypal.com/).",
                        validators=[
                            django.core.validators.RegexValidator(
                                message="URL must start with https://",
                                regex="^https://",
                            )
                        ],
                    ),
                ),
                (
                    "client_id",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Unique client ID provided by",
                            "the payment gateway for authentication.",
                        ),
                        max_length=255,
                    ),
                ),
                (
                    "client_secret",
                    models.CharField(
                        blank=True,
                        help_text="Client secret provided by the gateway.",
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(8)],
                    ),
                ),
                (
                    "webhook_id",
                    models.CharField(
                        blank=True,
                        help_text="webhook id/secret provided by the gateway.",
                        max_length=255,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]