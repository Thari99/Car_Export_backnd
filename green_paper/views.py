from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import GreenPaper
from .serializers import GreenPaperSerializer
from django.shortcuts import get_object_or_404

class GreenPaperView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all greenpapers ordered by latest update
    def get(self, request):
        greenpapers = GreenPaper.objects.all().order_by('-created_at')
        serializer = GreenPaperSerializer(greenpapers, many=True)
        return Response(serializer.data)

    # Create a new greenpaper record
    def post(self, request):
        serializer = GreenPaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GreenPaperDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk):
        return get_object_or_404(GreenPaper, pk=pk)

    # Retrieve a specific greenpaper by primary key
    def get(self, request, pk):
        greenpaper = self.get_object(pk)
        serializer = GreenPaperSerializer(greenpaper)
        return Response(serializer.data)

    # Update a greenpaper
    def put(self, request, pk):
        greenpaper = self.get_object(pk)
        serializer = GreenPaperSerializer(greenpaper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a greenpaper by ID
    def delete(self, request, pk):
        greenpaper = self.get_object(pk)
        greenpaper.delete()
        return Response(
            {"message": f"Green paper with id {pk} deleted successfully"},
            status=status.HTTP_200_OK
        )
