# Generated by Django 4.1.3 on 2023-01-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0020_alter_airwaybill_airport_of_destination"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airwaybill",
            name="Carrier_name",
            field=models.CharField(default=False, max_length=150, null=True),
        ),
    ]
