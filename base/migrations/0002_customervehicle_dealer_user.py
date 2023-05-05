# Generated by Django 4.1.7 on 2023-04-18 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customervehicle",
            name="dealer_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nondealer_customers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]