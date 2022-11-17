from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils import timezone
from django.urls import reverse


from .forms import Invoicetemplate

from .models import InvoiceLetter

# Create your views here.
def servicesInv(request):
    now = timezone.now()
    print(request.method)
    if request.method == 'POST':
        sent_data = request.POST
        print(sent_data)
        try:
            InvoiceLetter(
                from_companyname = sent_data.get('from_companyname'),
                from_personname = sent_data.get('from_personname'),
                from_address = sent_data.get('from_address'),
                from_phonenumber = sent_data.get('from_phonenumber'),
                from_sendertown = sent_data.get('from_town'),
                from_emailaddress = sent_data.get('from_emailaddress'),
                to_consigneeename = sent_data.get('to_consigneeename'),
                to_phonenumber = sent_data.get('to_phonenumber'),
                to_address = sent_data.get('to_address'),
                to_receivertown = sent_data.get('to_town'),
                # from_personname = sent_data.get('from_personname'),
                from_countries = sent_data.get('from_countries'),
                from_town = sent_data.get('from_town'),
                to_countries = sent_data.get('to_countries'),
                to_town = sent_data.get('to_town'),
                package_kind = sent_data.get('package_kind'),
                description = sent_data.get('description'),
                weight  = sent_data.get('weight'),
                length = sent_data.get('length'),
                width = sent_data.get('width'),
                height = sent_data.get('height'),
                airfreight_charges = sent_data.get('airfreight_charges'),
                other_charges = sent_data.get('other_charges'),
                insur_amount = sent_data.get('insur_amount'),
                nvd = sent_data.get('nvd'),
                ncv = sent_data.get('ncv'),
                handling_info = sent_data.get('handling_info')
            ).save()
        except Exception as e:
            print(f"Error saving the data:  {e}")
        return redirect('services-invoice')
    else:
        data =  {
            "from_companyname": "Equitexy Business Solutions",
            "from_personname": 'Boniface Mugwe'
        }
        form = Invoicetemplate(data=data)
        context = {
            'form': form,
            'data': data
        }
    
        return render(request, 'services/invoice.html', context)

def servicesAirway(request):
    context = {}

    return render(request, 'services/airwaybill.html', context)