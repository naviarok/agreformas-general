from django.db import models
import uuid

SERVICES = (
    ('Apartment renovations', 'Apartment renovations'),
    ('kitchen renovations', 'kitchen renovations'),
    ('Bathroom renovations', 'Bathroom renovations'),
    ('Bathroom renovations', 'Bathroom renovations'),
    ('General renovations', 'General renovations'),
    ('Wood carpentry', 'Wood carpentry'),
    ('Aluminum carpentry', 'Aluminum carpentry'),
    ('Floors', 'Floors'),
    ('Plasterboard placement', 'Plasterboard placement'),
)

class Conversion(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length = 100, choices = SERVICES, default = 'Apartment renovations', null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    def __str__(self) -> str:
        return self.fullname