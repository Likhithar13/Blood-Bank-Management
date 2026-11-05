from django import forms
from .models import Donor, BloodRequest, BloodStock

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ["name", "age", "blood_group", "phone", "city"]
        widgets = {"name": forms.TextInput(attrs={"placeholder": "Full name"}),
                   "phone": forms.TextInput(attrs={"placeholder": "Demo contact number"})}

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18 or age > 65:
            raise forms.ValidationError("For this demo, donor age must be between 18 and 65.")
        return age

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ["hospital_name", "contact_number", "blood_group", "units_required", "reason"]

class BloodStockForm(forms.ModelForm):
    class Meta:
        model = BloodStock
        fields = ["blood_group", "units"]
