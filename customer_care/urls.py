
from django.urls import path
from .views import ShippingStatusList, ShippingStatusDetail,EscalationDetail,EscalationList

urlpatterns = [
    path('shipping-status/', ShippingStatusList.as_view(), name='shipping-status-list'),
    path('shipping-status/<str:pk>/', ShippingStatusDetail.as_view(), name='shipping-status-detail'),
    path('escalations/', EscalationList.as_view(), name='escalation-list'),
    path('escalations/<str:pk>/', EscalationDetail.as_view(), name='escalation-detail'),
]
