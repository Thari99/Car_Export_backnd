
from django.urls import path
from .views import ShippingStatusList, ShippingStatusDetail

urlpatterns = [
    path('shipping-status/', ShippingStatusList.as_view(), name='shipping-status-list'),
    path('shipping-status/<str:pk>/', ShippingStatusDetail.as_view(), name='shipping-status-detail'),
]
