# Generated by Django 4.1.7 on 2023-04-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_additionaldocuments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="additionaldocuments",
            old_name="user",
            new_name="customervehicle",
        ),
    ]
