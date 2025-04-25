from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Quotation
from .serializers import QuotationSerializer


# QuotationList CRUD Views

class QuotationList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all Quotation ordered by latest update
    def get(self, request):
        quotations = Quotation.objects.all().order_by('-created_at')
        serializer = QuotationSerializer(quotations, many=True)
        return Response(serializer.data)

    # Create a new Quotation
    def post(self, request):
        data = request.data.copy()
        serializer = QuotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuotationDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Retrieve a specific Quotation by primary key
    def get_object(self, pk):
        try:
            return Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            raise Http404

    # View details of a specific Quotation
    def get(self, request, pk):
        record = self.get_object(pk)
        serializer = QuotationSerializer(record)
        return Response(serializer.data)

    # Full update (replace) of a Quotation
    def put(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = QuotationSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partial update of a Quotation
    def patch(self, request, pk):
        record = self.get_object(pk)
        data = request.data.copy()
        serializer = QuotationSerializer(record, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a Quotation by ID
    def delete(self, request, pk):
        record = self.get_object(pk)
        record.delete()
        return Response( 
            {"message": f"Quotation with id {pk} deleted successfully"},
              status=status.HTTP_200_OK
            )