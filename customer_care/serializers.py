

from rest_framework import serializers
from .models import ShippingStatus

class ShippingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingStatus
        fields = '__all__'
