
from django.urls import path
from .views import ShippingStatusList, ShippingStatusDetail,EscalationDetail,EscalationList,ResolveIssueList,ResolveIssueDetail

urlpatterns = [
    path('shipping-status/', ShippingStatusList.as_view(), name='shipping-status-list'),
    path('shipping-status/<str:pk>/', ShippingStatusDetail.as_view(), name='shipping-status-detail'),

    path('escalations/', EscalationList.as_view(), name='escalation-list'),
    path('escalations/<str:pk>/', EscalationDetail.as_view(), name='escalation-detail'),

    path('resolved-issues/', ResolveIssueList.as_view(), name='resolved-issue-list'),
    path('resolved-issues/<str:pk>/', ResolveIssueDetail.as_view(), name='resolved-issue-detail'),
]
