# Generated by Django 4.1.3 on 2023-01-03 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0011_alter_airwaybill_flight_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="airwaybill",
            name="flight_date",
        ),
    ]