# Generated by Django 4.1.7 on 2023-04-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_remove_customervehicle_dealer_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicleinformation",
            name="Dealership",
        ),
        migrations.RemoveField(
            model_name="vehicleinformation",
            name="dealer_user",
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="dealer",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]