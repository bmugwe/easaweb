from contextlib import ContextDecorator
from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from services.models import InvoiceLetter, airwaybill


# Create your views here.
def homepage(request):
    context = {}
    return render(request, "user/homepage.html", context)


@login_required
def index(request):
    currentuser = request.user
    userinstance = User.objects.get(username=currentuser)
    currentInvoice = InvoiceLetter.objects.filter(user_saved_by_id=userinstance.id)

    print(currentInvoice)
    context = {"currentInvoice": currentInvoice}
    return render(request, "dashboard/index.html", context)


@login_required
def staff(request):
    return render(request, "dashboard/staff.html")


@login_required
def products(request):
    currentInvoice = airwaybill.objects.filter(is_void=False)
    currentInvoice = currentInvoice.filter(is_deleted=False)
    currentInvoice = currentInvoice.filter(is_processed=False)
    print(currentInvoice)
    context = {"currentInvoice": currentInvoice}

    return render(request, "dashboard/products.html", context)


@login_required
def orders(request):
    currentuser = request.user
    userinstance = User.objects.get(username=currentuser)

    currentInvoice = InvoiceLetter.objects.filter(
        is_void=False, is_deleted=False, is_processed=False
    )
    print(currentInvoice)
    context = {"currentInvoice": currentInvoice}
    return render(request, "dashboard/orders.html", context)


@login_required
def profile(request):
    return render(request, "dashboard/profile.html")


@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")
