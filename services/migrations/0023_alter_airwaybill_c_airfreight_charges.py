# Generated by Django 4.1.3 on 2023-01-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0022_alter_airwaybill_requested_routing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airwaybill",
            name="c_airfreight_charges",
            field=models.FloatField(default=0, null=True),
        ),
    ]
