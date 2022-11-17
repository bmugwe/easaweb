from django.db import models
import datetime
from django.utils import timezone
import uuid

# Create your models here.

class InvoiceLetter(models.Model):
    inv_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    description = models.CharField(max_length=1500)
    weight  = models.CharField(max_length=15)
    length = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    height = models.CharField(max_length=150)
    airfreight_charges = models.CharField(max_length=150)
    other_charges = models.CharField(max_length=150)
    insur_amount = models.CharField(max_length=150)
    nvd = models.CharField(max_length=150)
    ncv = models.CharField(max_length=150)
    handling_info  = models.CharField(max_length=150)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    timestamp_updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "invoice_letter"

    def __unicode__(self):
        return str(self.inv_id, self.from_companyname)