# Generated by Django 4.2.1 on 2023-05-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient_records", "0002_alter_billing_options_alter_drugs_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctors",
            name="patient_treated",
        ),
        migrations.AlterField(
            model_name="patient",
            name="doctor_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="patient_records.doctors",
                verbose_name=" Attending Doctor's Name",
            ),
        ),
    ]
