# urls.py

from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # Customer URLs
    path('customers/', views.CustomerListView, name='customer-list'),
    # path('customers/<int:pk>/', views.CustomerDetailView, name='customer-detail'),

    # Seed URLs
    path('seeds/', views.SeedListView, name='seed-list'),
    path('test/', views.test, name='seed-list'),
    # path('seeds/<int:pk>/', views.SeedDetailView, name='seed-detail'),
    path('seed-total-sales/', views.SaleListViewTotal.as_view(), name='seed-total-sales'),
    path('seed-total/', views.test, name='seed-total'),

    # Purchase URLs
    path('purchases/', views.PurchaseListView, name='purchase-list'),
    path('purchases/<int:id>/', views.PurchaseByCustomer.as_view()),
    # path('purchases/<int:pk>/', views.PurchaseDetailView, name='purchase-detail'),
    path('sales/', views.SaleListView, name='sale-list'),
    path('sales/<int:id>/', views.SalesByCustomer.as_view()),
]
