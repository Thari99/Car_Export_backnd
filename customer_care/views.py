
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import ShippingStatus,Escalation
from .serializers import ShippingStatusSerializer, EscalationSerializer


# ShippingStatus CRUD Views

class ShippingStatusList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all shipping statuses ordered by latest update
    def get(self, request):
        statuses = ShippingStatus.objects.all().order_by('-updated_at')
        serializer = ShippingStatusSerializer(statuses, many=True)
        return Response(serializer.data)

    # Create a new shipping status
    def post(self, request):
        data = request.data.copy()
        serializer = ShippingStatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingStatusDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Retrieve a specific shipping status by primary key
    def get_object(self, pk):
        try:
            return ShippingStatus.objects.get(pk=pk)
        except ShippingStatus.DoesNotExist:
            raise Http404

    # View details of a specific shipping status
    def get(self, request, pk):
        record = self.get_object(pk)
        serializer = ShippingStatusSerializer(record)
        return Response(serializer.data)

    # Full update (replace) of a shipping status
    def put(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = ShippingStatusSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partial update of a shipping status
    def patch(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = ShippingStatusSerializer(record, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a shipping status by ID
    def delete(self, request, pk):
        record = self.get_object(pk)
        record.delete()
        return Response({"message": f"Shipping status with id {pk} deleted successfully"}, status=status.HTTP_200_OK)

# Escalation CRUD Views
class EscalationList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all escalations ordered by creation time
    def get(self, request):
        escalations = Escalation.objects.all().order_by('-created_at')
        serializer = EscalationSerializer(escalations, many=True)
        return Response(serializer.data)

    # Create a new escalation record
    def post(self, request):
        serializer = EscalationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EscalationDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Retrieve a specific escalation by primary key
    def get_object(self, pk):
        try:
            return Escalation.objects.get(pk=pk)
        except Escalation.DoesNotExist:
            raise Http404

    # View details of a specific escalation
    def get(self, request, pk):
        record = self.get_object(pk)
        serializer = EscalationSerializer(record)
        return Response(serializer.data)

    # Full update (replace) of an escalation
    def put(self, request, pk):
        record = self.get_object(pk)
        serializer = EscalationSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partial update of an escalation
    def patch(self, request, pk):
        record = self.get_object(pk)
        serializer = EscalationSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete an escalation by ID
    def delete(self, request, pk):
        record = self.get_object(pk)
        record.delete()
        return Response({"message": f"Escalation with id {pk} deleted successfully"}, status=status.HTTP_200_OK)
