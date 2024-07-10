# Market/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('contact/', views.contact_view, name='contact'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('payment/', views.payment, name='payment'), 
    
    
    path('index/freshfish/', views.fresh_fish_view, name='freshfish'),
    path('freshshellfish/', views.fresh_shellfish_view, name='freshshellfish'),
    path('frozenshellfish/', views.frozen_shellfish_view, name='frozenshellfish'),

    path('adminpg/', views.admin_page_view, name='adminpg'),
    path('addorder/', views.add_order, name='addorder'),
    path('addstock/', views.add_order, name='addstock'),
    path('create_order/', views.create_order, name='admin'),


]
