# Generated by Django 4.1.7 on 2023-04-08 01:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_user_dealer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dealer_id",
            field=models.UUIDField(
                blank=True, default=uuid.uuid4, editable=False, null=True, unique=True
            ),
        ),
    ]
