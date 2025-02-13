# Generated by Django 4.2.6 on 2024-01-19 03:30

from django.db import migrations, models
import django.db.models.deletion
import uuid
import zango.apps.dynamic_models.fields
import zango.core.storage_utils


class Migration(migrations.Migration):
    dependencies = [
        ("appauth", "0005_remove_appusermodel_user"),
        (
            "dynamic_models",
            "frame_0002_framesmodel_object_uuid",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ExportJob",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "object_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("filename", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "file",
                    zango.core.storage_utils.ZFileField(
                        blank=True,
                        null=True,
                        upload_to=zango.core.storage_utils.RandomUniqueFileName,
                        validators=[zango.core.storage_utils.validate_file_extension],
                    ),
                ),
                ("export_metadata", models.JSONField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("processing", "Processing"),
                            ("completed", "Completed"),
                            ("failed", "Failed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "export_type",
                    models.CharField(
                        choices=[("xlsx", "Excel Export"), ("csv", "CSV Export")],
                        max_length=20,
                    ),
                ),
                (
                    "celery_task_id",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
                (
                    "user",
                    zango.apps.dynamic_models.fields.ZForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="appauth.appusermodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
