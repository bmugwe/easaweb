from contextlib import ContextDecorator
from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from services.models import InvoiceLetter
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'user/homepage.html',context)


@login_required
def index(request):
    context = {}
    return render(request, 'dashboard/index.html',context)

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def products(request):
    return render(request, 'dashboard/products.html')

@login_required
def orders(request):
    currentInvoice = InvoiceLetter.objects.filter(is_void=False)
    currentInvoice = currentInvoice.filter(is_deleted=False)
    currentInvoice = currentInvoice.filter(is_processed=False)
    print(currentInvoice)
    context= {
        "currentInvoice": currentInvoice
    }
    return render(request, 'dashboard/orders.html', context)

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')