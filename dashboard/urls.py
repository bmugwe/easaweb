from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('dashboard/', views.dashboard, name='dashboard-dashboard'),
    path('profile', views.profile, name='dashboard-profile'),
    path('products', views.products, name='dashboard-products'),
    path('orders', views.orders, name='dashboard-orders'),

]
