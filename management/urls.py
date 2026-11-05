from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("donors/", views.donor_list, name="donor_list"),
    path("donors/add/", views.donor_add, name="donor_add"),
    path("inventory/", views.inventory, name="inventory"),
    path("inventory/add/", views.stock_add, name="stock_add"),
    path("requests/", views.request_list, name="request_list"),
    path("requests/add/", views.request_add, name="request_add"),
]
