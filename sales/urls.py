from django.urls import path
from .views import QuotationList, QuotationDetail

urlpatterns = [
    path('QuotationList/', QuotationList.as_view(), name='Quotation-List'),
    path('QuotationList/<str:pk>/', QuotationDetail.as_view(), name='Quotation-Detail'),
    ]