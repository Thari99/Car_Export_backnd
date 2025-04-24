

from rest_framework import serializers
from .models import ShippingStatus, Escalation

class ShippingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingStatus
        fields = '__all__'

class EscalationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escalation
        fields = '__all__'
