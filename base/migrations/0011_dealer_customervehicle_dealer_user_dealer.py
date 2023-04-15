# Generated by Django 4.1.7 on 2023-04-12 20:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_remove_user_dealer_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dealer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "dealer_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customervehicle",
            name="dealer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="financing_requests",
                to="base.dealer",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="dealer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customers",
                to="base.dealer",
            ),
        ),
    ]
