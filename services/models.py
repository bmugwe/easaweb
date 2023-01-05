from django.db import models
import datetime
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

# Create your models here.


class InvoiceLetter(models.Model):
    inv_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_companyname = models.CharField(max_length=150)
    from_personname = models.CharField(max_length=150)
    from_address = models.CharField(max_length=150)
    from_emailaddress = models.CharField(max_length=150)
    from_phonenumber = models.CharField(max_length=150)
    from_sendertown = models.CharField(max_length=150)
    from_emailaddress = models.CharField(max_length=150)
    to_consigneeename = models.CharField(max_length=150)
    to_phonenumber = models.CharField(max_length=150)
    to_address = models.CharField(max_length=150)
    to_receivertown = models.CharField(max_length=150)
    from_countries = models.CharField(max_length=150)
    from_town = models.CharField(max_length=150)
    to_countries = models.CharField(max_length=150)
    to_town = models.CharField(max_length=150)
    package_kind = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1500)
    weight = models.CharField(max_length=15)
    length = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    height = models.CharField(max_length=150)
    airfreight_charges = models.CharField(max_length=150)
    other_charges = models.CharField(max_length=150)
    insur_amount = models.CharField(max_length=150)
    nvd = models.CharField(max_length=150)
    ncv = models.CharField(max_length=150)
    handling_info = models.CharField(max_length=150)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    user_saved_by = models.ForeignKey(
        User, verbose_name=("inventryuser"), on_delete=models.CASCADE
    )
    # assigned_to = models.ForeignKey(User, verbose_name=("assigneduser"), on_delete=models.CASCADE)
    timestamp_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invoice_letter"

    def __unicode__(self):
        return str(self.inv_id, self.from_companyname)


# class Tracking(models.Model):
#     tr_id = models.UUIDField(primary_key = True, default=uuid.uuid4,editable=False)
#     inv_id = models.ForeignKey(InvoicLetter, verbose_name=_("tracker_locate"), on_delete=models.CASCADE)
#     # timestamp_arrived =


#     class Meta:
#         db_table = "parcel_tracker"

#     def __unicode__(self):
#         return str(self.inv_id, self.from_companyname)


class airwaybill(models.Model):
    awb_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inv_id = models.ForeignKey(
        InvoiceLetter, verbose_name=("inv_awb_fk"), on_delete=models.CASCADE
    )
    from_companyname = models.CharField(max_length=150)
    from_personname = models.CharField(max_length=150)
    from_address = models.CharField(max_length=150)
    from_phonenumber = models.CharField(max_length=150)
    from_sendertown = models.CharField(max_length=150)
    from_emailaddress = models.CharField(max_length=150)
    to_consigneeename = models.CharField(max_length=150)
    to_phonenumber = models.CharField(max_length=150)
    to_address = models.CharField(max_length=150)
    to_receivertown = models.CharField(max_length=150)
    from_countries = models.CharField(max_length=150)
    from_town = models.CharField(max_length=150)
    to_countries = models.CharField(max_length=150)
    to_town = models.CharField(max_length=150)
    package_kind = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1500)
    weight = models.CharField(max_length=15)
    length = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    height = models.CharField(max_length=150)
    airfreight_charges = models.CharField(max_length=150, null=True)
    other_charges = models.CharField(max_length=150, null=True)
    insur_amount = models.CharField(max_length=150, null=True)
    nvd = models.CharField(max_length=150, null=True)
    ncv = models.CharField(max_length=150, null=True)
    handling_info = models.CharField(max_length=150, null=True)
    flight_date = models.DateTimeField(default=timezone.now)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    user_saved_by = models.ForeignKey(
        User, verbose_name=("inventryuser"), on_delete=models.CASCADE
    )
    # assigned_to = models.ForeignKey(User, verbose_name=("assigneduser"), on_delete=models.CASCADE)
    timestamp_updated = models.DateTimeField(auto_now=True)
    Airport_of_departure= models.CharField(max_length=150, default=False, null=True)
    AIRPORT_OF_DEST= models.CharField(max_length=150, default=False, null=True)
    Airport_of_destination= models.CharField(max_length=150, default=False, null=True)
    c_airfreight_charges= models.FloatField(default=0, null=True)
    c_charges_dest= models.FloatField(default=0)
    c_other_charges_agent= models.FloatField(default=0)
    c_other_charges_carrier= models.FloatField(default=0)
    c_total_charges = models.FloatField(default=0)
    c_tax = models.FloatField(default=0)
    c_valuation_charges = models.FloatField(default=0)
    Carrier_name = models.CharField(max_length=150, default=False, null=True)
    cheargeable_weight = models.FloatField(default=0)
    commodity_item_no = models.CharField(max_length=150, default=False)
    FIRST_CARRIER = models.CharField(max_length=150, default=False)
    IATA_ACCNO = models.CharField(max_length=150, default=False)
    IATA_CITY = models.CharField(max_length=150, default=False)
    IATA_CODE = models.CharField(max_length=150, default=False)
    IATA_NAME = models.CharField(max_length=150, default=False)
    other_charges_2 = models.FloatField(default=0, null=True)
    p_airfreight_charges = models.FloatField(default=0)
    p_charges_dest = models.FloatField(default=0)
    p_currency_conversion = models.FloatField(default=0)
    p_other_charges_agent = models.FloatField(default=0)
    p_other_charges_carrier = models.FloatField(default=0)
    p_tax = models.FloatField(default=0)
    p_total_charges = models.FloatField(default=0)
    p_valuation_charges = models.FloatField(default=0)
    Rate_charge = models.FloatField(default=0)
    Requested_routing = models.CharField(max_length=150, default=False, null=True)
    ROUTING_DEST = models.CharField(max_length=150, default=False)
    total_charge = models.FloatField(default=0)


    class Meta:
        db_table = "airwaybill"

    def __unicode__(self):
        return str(self.awb_id, self.from_companyname)
