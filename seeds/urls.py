# urls.py

from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # Customer URLs
    path('customers/', views.CustomerListView, name='customer-list'),

    # Seed URLs
    path('seeds/', views.SeedListView, name='seed-list'),
    path('test/', views.test, name='seed-list'),
    path('seed-total-sales/', views.SaleListViewTotal.as_view(), name='seed-total-sales'),
    path('seed-total/', views.test, name='seed-total'),

    # Purchase URLs
    path('purchases/', views.PurchaseListView, name='purchase-list'),
    path('purchases/<int:id>/', views.PurchaseByCustomer.as_view()),

    # Sales URLs
    path('sales/', views.SaleListView, name='sale-list'),
    path('sales/<int:id>/', views.SalesByCustomer.as_view()),

    # Feed URLs
    path('feeds/', views.FeedListView, name='purchase-list'),
    path('feeds/<int:id>/', views.FeedByCustomer.as_view()),
    # path('purchases/<int:id>/', views.PurchaseByCustomer.as_view()),
]
