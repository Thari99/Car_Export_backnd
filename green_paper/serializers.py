from rest_framework import serializers
from .models import GreenPaper

class GreenPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenPaper
        fields = '__all__'
