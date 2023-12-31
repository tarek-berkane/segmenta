# Generated by Django 4.2.7 on 2023-11-15 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagetemporary",
            name="add_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="temporary_images",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="add_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
