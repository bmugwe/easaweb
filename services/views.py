from django.shortcuts import render

# Create your views here.
def servicesInv(request):
    context = {}

    return render(request, 'services/invoice.html', context)