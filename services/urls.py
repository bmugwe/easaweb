from django.urls import path
from . import views


urlpatterns = [
    path('invoice', views.servicesInv, name='services-invoice'),
    path('airwaybill/<uuid:id>/', views.servicesAirway, name='services_airway'),
    path('printinvoice/<uuid:id>/', views.print_invoice, name='invoiceprint'),
    path('airwaybill_invoice/<uuid:id>/', views.generateAirwaybill, name="generate_airwaybill")
]
