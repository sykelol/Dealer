# Generated by Django 4.1.7 on 2023-04-18 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_customervehicle_dealer_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customervehicle",
            name="dealer_user",
        ),
        migrations.AddField(
            model_name="customervehicle",
            name="dealer_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="dealer_vehicles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
