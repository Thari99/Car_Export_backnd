from django.db import models
from django.conf import settings
from django.utils import timezone

class ShippingStatus(models.Model):

    order_id = models.CharField(max_length=255, primary_key=True)
    customer = models.CharField(max_length=255)
    current_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    escalation_note = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.new_status}"

class Escalation(models.Model):
    escalation_id = models.CharField(max_length=10, primary_key=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    issue_type = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    assigned_to = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='open')
    customer_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)    
    priority = models.CharField(max_length=20)   
    updated_at = models.DateTimeField()  
    description = models.TextField()

    def __str__(self):
        return f"{self.escalation_id} - {self.customer_name}"

class ResolveIssue(models.Model):
    escalation_id = models.CharField(max_length=10, primary_key=True)
    customer_name = models.CharField(max_length=100)
    resolution_type = models.EmailField()
    resolution_note = models.CharField(max_length=100)
    notify_customer = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.escalation_id}"