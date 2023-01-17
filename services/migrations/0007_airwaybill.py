# Generated by Django 4.1.3 on 2023-01-15 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0006_delete_airwaybill'),
    ]

    operations = [
        migrations.CreateModel(
            name='airwaybill',
            fields=[
                ('awb_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_companyname', models.CharField(max_length=150)),
                ('from_personname', models.CharField(max_length=150)),
                ('from_address', models.CharField(max_length=150)),
                ('from_phonenumber', models.CharField(max_length=150)),
                ('from_sendertown', models.CharField(max_length=150)),
                ('from_emailaddress', models.CharField(max_length=150)),
                ('to_consigneeename', models.CharField(max_length=150)),
                ('to_phonenumber', models.CharField(max_length=150)),
                ('to_address', models.CharField(max_length=150)),
                ('to_receivertown', models.CharField(max_length=150)),
                ('from_countries', models.CharField(max_length=150)),
                ('from_town', models.CharField(max_length=150)),
                ('to_countries', models.CharField(max_length=150)),
                ('to_town', models.CharField(max_length=150)),
                ('package_kind', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=1500)),
                ('weight', models.CharField(max_length=15)),
                ('length', models.CharField(max_length=150)),
                ('width', models.CharField(max_length=150)),
                ('height', models.CharField(max_length=150)),
                ('airfreight_charges', models.CharField(max_length=150, null=True)),
                ('other_charges', models.CharField(max_length=150, null=True)),
                ('insur_amount', models.CharField(max_length=150, null=True)),
                ('nvd', models.CharField(max_length=150, null=True)),
                ('ncv', models.CharField(max_length=150, null=True)),
                ('handling_info', models.CharField(max_length=150, null=True)),
                ('flight_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_processed', models.BooleanField(default=False)),
                ('accept', models.BooleanField(default=False)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('Airport_of_departure', models.CharField(default=False, max_length=150, null=True)),
                ('AIRPORT_OF_DEST', models.CharField(default=False, max_length=150, null=True)),
                ('Airport_of_destination', models.CharField(default=False, max_length=150, null=True)),
                ('c_airfreight_charges', models.FloatField(default=0, null=True)),
                ('c_charges_dest', models.FloatField(default=0)),
                ('c_other_charges_agent', models.FloatField(default=0)),
                ('c_other_charges_carrier', models.FloatField(default=0)),
                ('c_total_charges', models.FloatField(default=0)),
                ('c_tax', models.FloatField(default=0)),
                ('c_valuation_charges', models.FloatField(default=0)),
                ('Carrier_name', models.CharField(default=False, max_length=150, null=True)),
                ('cheargeable_weight', models.FloatField(default=0)),
                ('commodity_item_no', models.CharField(default=False, max_length=150)),
                ('FIRST_CARRIER', models.CharField(default=False, max_length=150)),
                ('IATA_ACCNO', models.CharField(default=False, max_length=150)),
                ('IATA_CITY', models.CharField(default=False, max_length=150)),
                ('IATA_CODE', models.CharField(default=False, max_length=150)),
                ('IATA_NAME', models.CharField(default=False, max_length=150)),
                ('other_charges_2', models.FloatField(default=0, null=True)),
                ('p_airfreight_charges', models.FloatField(default=0)),
                ('p_charges_dest', models.FloatField(default=0)),
                ('p_currency_conversion', models.FloatField(default=0)),
                ('p_other_charges_agent', models.FloatField(default=0)),
                ('p_other_charges_carrier', models.FloatField(default=0)),
                ('p_tax', models.FloatField(default=0)),
                ('p_total_charges', models.FloatField(default=0)),
                ('p_valuation_charges', models.FloatField(default=0)),
                ('Rate_charge', models.FloatField(default=0)),
                ('Requested_routing', models.CharField(default=False, max_length=150, null=True)),
                ('ROUTING_DEST', models.CharField(default=False, max_length=150)),
                ('total_charge', models.FloatField(default=0)),
                ('inv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.invoiceletter', verbose_name='inv_awb_fk')),
                ('user_saved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='inventryuser')),
            ],
            options={
                'db_table': 'airwaybill',
            },
        ),
    ]
