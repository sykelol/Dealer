# Generated by Django 4.1.7 on 2023-04-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_alter_additionaldocuments_customervehicle"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="additional_documents",
            field=models.FileField(
                blank=True, null=True, upload_to="additional_documents"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="paystub",
            field=models.FileField(blank=True, null=True, upload_to="paystub"),
        ),
        migrations.AddField(
            model_name="user",
            name="tax_return",
            field=models.FileField(blank=True, null=True, upload_to="tax_return"),
        ),
        migrations.DeleteModel(
            name="AdditionalDocuments",
        ),
    ]
