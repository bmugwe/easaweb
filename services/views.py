from django.shortcuts import render
from .forms import Invoicetemplate

# Create your views here.
def servicesInv(request):

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