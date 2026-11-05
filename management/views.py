from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor, BloodStock, BloodRequest
from .forms import DonorForm, BloodRequestForm, BloodStockForm

def dashboard(request):
    context = {
        "donor_count": Donor.objects.count(),
        "request_count": BloodRequest.objects.count(),
        "stock_count": sum(BloodStock.objects.values_list("units", flat=True)),
        "recent_requests": BloodRequest.objects.order_by("-created_at")[:5],
    }
    return render(request, "management/dashboard.html", context)

def donor_list(request):
    return render(request, "management/donor_list.html", {"donors": Donor.objects.order_by("-created_at")})

def donor_add(request):
    form = DonorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Donor record saved.")
        return redirect("donor_list")
    return render(request, "management/form.html", {"form": form, "heading": "Register Donor"})

def inventory(request):
    return render(request, "management/inventory.html", {"stocks": BloodStock.objects.order_by("blood_group")})

def stock_add(request):
    # A stock record is an illustrative inventory entry, not a clinical release record.
    form = BloodStockForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        existing = BloodStock.objects.filter(blood_group=obj.blood_group).first()
        if existing:
            existing.units = obj.units
            existing.save()
        else:
            obj.save()
        messages.success(request, "Inventory record saved.")
        return redirect("inventory")
    return render(request, "management/form.html", {"form": form, "heading": "Add / Update Blood Stock"})

def request_list(request):
    return render(request, "management/request_list.html", {"requests": BloodRequest.objects.order_by("-created_at")})

def request_add(request):
    form = BloodRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        blood_request = form.save(commit=False)
        # This is only a simple exact-label stock lookup for demonstration.
        # It does NOT determine donor compatibility or authorize blood issue.
        stock = BloodStock.objects.filter(blood_group=blood_request.blood_group).first()
        if stock and stock.units >= blood_request.units_required:
            blood_request.status = "AVAILABLE"
        else:
            blood_request.status = "INSUFFICIENT"
        blood_request.save()
        messages.success(request, "Request recorded. A qualified professional must verify all clinical details.")
        return redirect("request_list")
    return render(request, "management/form.html", {"form": form, "heading": "Create Emergency Request"})
