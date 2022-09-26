from contextlib import ContextDecorator
from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    context = {}       

    return render(request, 'dashboard/index.html',context)


def staff(request):
    return render(request, 'dashboard/staff.html')

def products(request):
    return render(request, 'dashboard/products.html')


def orders(request):
    return render(request, 'dashboard/orders.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')