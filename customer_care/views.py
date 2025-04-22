
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import ShippingStatus
from .serializers import ShippingStatusSerializer

class ShippingStatusList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        statuses = ShippingStatus.objects.all().order_by('-updated_at')
        serializer = ShippingStatusSerializer(statuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        serializer = ShippingStatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingStatusDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return ShippingStatus.objects.get(pk=pk)
        except ShippingStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        record = self.get_object(pk)
        serializer = ShippingStatusSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = ShippingStatusSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = ShippingStatusSerializer(record, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        record = self.get_object(pk)
        record.delete()
        return Response({"message": f"Shipping status with id {pk} deleted successfully"}, status=status.HTTP_200_OK)
