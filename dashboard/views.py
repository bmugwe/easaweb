from contextlib import ContextDecorator
from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

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
    return render(request, 'dashboard/orders.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')