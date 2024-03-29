# Generated by Django 4.2 on 2023-05-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0016_alter_user_drivers_license"),
    ]

    operations = [
        migrations.AddField(
            model_name="customervehicle",
            name="bill_of_sale",
            field=models.FileField(blank=True, null=True, upload_to="bill_of_sale"),
        ),
        migrations.AddField(
            model_name="customervehicle",
            name="car_ownership",
            field=models.FileField(blank=True, null=True, upload_to="car_ownership"),
        ),
        migrations.AddField(
            model_name="customervehicle",
            name="loan_agreement",
            field=models.FileField(blank=True, null=True, upload_to="loan_agreement"),
        ),
        migrations.AddField(
            model_name="user",
            name="bank_statement",
            field=models.FileField(blank=True, null=True, upload_to="bank_statement"),
        ),
        migrations.AddField(
            model_name="user",
            name="employment_letter",
            field=models.FileField(
                blank=True, null=True, upload_to="employment_letter"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="proof_of_insurance",
            field=models.FileField(
                blank=True, null=True, upload_to="proof_of_insurance"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="void_cheque",
            field=models.FileField(blank=True, null=True, upload_to="void_cheque"),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="bank_statement",
            field=models.FileField(blank=True, null=True, upload_to="bank_statement"),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="bill_of_sale",
            field=models.FileField(blank=True, null=True, upload_to="bill_of_sale"),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="car_ownership",
            field=models.FileField(blank=True, null=True, upload_to="car_ownership"),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="employment_letter",
            field=models.FileField(
                blank=True, null=True, upload_to="employment_letter"
            ),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="loan_agreement",
            field=models.FileField(blank=True, null=True, upload_to="loan_agreement"),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="proof_of_insurance",
            field=models.FileField(
                blank=True, null=True, upload_to="proof_of_insurance"
            ),
        ),
        migrations.AddField(
            model_name="vehicleinformation",
            name="void_cheque",
            field=models.FileField(blank=True, null=True, upload_to="void_cheque"),
        ),
    ]
