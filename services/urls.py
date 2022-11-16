from django.urls import path
from . import views


urlpatterns = [
    path('invoice', views.servicesInv, name='services-invoice'),
]
