# Generated by Django 4.2 on 2023-04-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0014_alter_customervehicle_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customervehicle",
            name="progress",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name="vehicleinformation",
            name="progress",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
