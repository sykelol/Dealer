# Generated by Django 4.1.7 on 2023-03-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="vehicleinformation",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
