# Generated by Django 4.1.7 on 2023-04-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0013_remove_customervehicle_dealer_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="dealer_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
