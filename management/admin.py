from django.contrib import admin
from .models import Donor, BloodStock, BloodRequest

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ("name", "blood_group", "age", "city", "created_at")
    search_fields = ("name", "phone", "city")

@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ("blood_group", "units", "updated_at")

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ("hospital_name", "blood_group", "units_required", "status", "created_at")
    list_filter = ("status", "blood_group")
