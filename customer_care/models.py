from django.db import models
from django.conf import settings

class ShippingStatus(models.Model):

    order_id = models.CharField(max_length=255, primary_key=True)
    customer = models.CharField(max_length=255)
    current_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    escalation_note = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.new_status}"
