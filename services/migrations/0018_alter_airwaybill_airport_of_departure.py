# Generated by Django 4.1.3 on 2023-01-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0017_alter_airwaybill_rate_charge_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airwaybill",
            name="Airport_of_departure",
            field=models.CharField(default=False, max_length=150, null=True),
        ),
    ]