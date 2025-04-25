from django.db import models
from django.utils import timezone

class Quotation(models.Model):
    vehicle_model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    additional_specifications = models.CharField(max_length=255)
    engine_number = models.IntegerField()
    manufacturing_year = models.IntegerField()
    variant = models.CharField(max_length=255)
    fob_price = models.CharField(max_length=100)
    cif_price = models.CharField(max_length=100)
    shipping_port = models.CharField(max_length=255)
    dilivery_time = models.IntegerField()  
    currency = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.id}"