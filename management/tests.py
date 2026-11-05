from django.test import TestCase
from django.urls import reverse
from .models import Donor, BloodStock, BloodRequest

class BloodBankTests(TestCase):
    def test_dashboard_loads(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_donor_registration(self):
        response = self.client.post(reverse("donor_add"), {
            "name": "Demo Donor", "age": 25, "blood_group": "O+",
            "phone": "9000000000", "city": "Bengaluru"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Donor.objects.count(), 1)

    def test_donor_age_validation(self):
        response = self.client.post(reverse("donor_add"), {
            "name": "Underage Demo", "age": 16, "blood_group": "A+",
            "phone": "9000000001", "city": "Bengaluru"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Donor.objects.count(), 0)

    def test_emergency_request_checks_recorded_stock(self):
        BloodStock.objects.create(blood_group="B+", units=5)
        response = self.client.post(reverse("request_add"), {
            "hospital_name": "Demo Hospital", "contact_number": "9000000002",
            "blood_group": "B+", "units_required": 3, "reason": "Demo request"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BloodRequest.objects.first().status, "AVAILABLE")
