# Generated by Django 4.1.4 on 2022-12-31 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_customerinformation_social_insurance_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerinformation",
            name="phone_number",
            field=models.CharField(max_length=10),
        ),
    ]
