from django.urls import path
from .views import GreenPaperView, GreenPaperDetails

urlpatterns = [
    path('greenpaper/', GreenPaperView.as_view(), name='quotation-list-create'),
    path('greenpaper/<int:pk>/', GreenPaperDetails.as_view(), name='quotation-detail'),
]
