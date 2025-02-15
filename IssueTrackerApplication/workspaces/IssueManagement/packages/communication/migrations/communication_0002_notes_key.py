# Generated by Django 4.2.11 on 2024-04-09 10:49

from django.db import migrations, models
import django.db.models.deletion
import uuid
import zango.apps.dynamic_models.fields
import zango.core.storage_utils


class Migration(migrations.Migration):
    dependencies = [
        ("appauth", "0006_appusermodel_app_objects"),
        ("dynamic_models", "communication_0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="telephonyconfigmodel",
            name="notes_key",
            field=models.CharField(default="telephony_notes", max_length=100),
        ),
        migrations.AlterField(
            model_name="smstransactionsmodel",
            name="src",
            field=models.CharField(max_length=20, null=True, verbose_name="Source"),
        ),
    ]
