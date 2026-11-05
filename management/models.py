from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

BLOOD_GROUPS = [
    ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
    ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-"),
]

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, unique=True)
    units = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blood_group}: {self.units} units"

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("AVAILABLE", "Stock recorded as available - verification required"),
        ("INSUFFICIENT", "Insufficient recorded stock"),
    ]
    hospital_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_required = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    reason = models.CharField(max_length=250)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.hospital_name} - {self.blood_group}"
