# Generated by Django 4.1.3 on 2023-01-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0014_remove_airwaybill_airport_of_dest_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="airwaybill",
            name="AIRPORT_OF_DEST",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="Airport_of_departure",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="Airport_of_destination",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="Carrier_name",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="FIRST_CARRIER",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="IATA_ACCNO",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="IATA_CITY",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="IATA_CODE",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="IATA_NAME",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="ROUTING_DEST",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="Rate_charge",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="Requested_routing",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="accept",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_airfreight_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_charges_dest",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_other_charges_agent",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_other_charges_carrier",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_tax",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_total_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="c_valuation_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="cheargeable_weight",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="commodity_item_no",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="other_charges_2",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_airfreight_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_charges_dest",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_currency_conversion",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_other_charges_agent",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_other_charges_carrier",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_tax",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_total_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="p_valuation_charges",
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name="airwaybill",
            name="total_charge",
            field=models.CharField(default=False, max_length=150),
        ),
    ]