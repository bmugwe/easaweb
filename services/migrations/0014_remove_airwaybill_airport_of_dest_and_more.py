# Generated by Django 4.1.3 on 2023-01-03 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0013_airwaybill_flight_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="airwaybill",
            name="AIRPORT_OF_DEST",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="Airport_of_departure",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="Airport_of_destination",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="Carrier_name",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="FIRST_CARRIER",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="IATA_ACCNO",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="IATA_CITY",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="IATA_CODE",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="IATA_NAME",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="ROUTING_DEST",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="Rate_charge",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="Requested_routing",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="accept",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_airfreight_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_charges_dest",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_other_charges_agent",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_other_charges_carrier",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_tax",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_total_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="c_valuation_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="cheargeable_weight",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="commodity_item_no",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="other_charges_2",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_airfreight_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_charges_dest",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_currency_conversion",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_other_charges_agent",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_other_charges_carrier",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_tax",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_total_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="p_valuation_charges",
        ),
        migrations.RemoveField(
            model_name="airwaybill",
            name="total_charge",
        ),
    ]
