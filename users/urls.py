from django.urls import path
from .views import RegisterView, LoginView, SuperAdminOnlyView, AdminOnlyView, UserOnlyView,AdminOrSupperAdminOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('super-admin/', SuperAdminOnlyView.as_view(), name='super-admin'),
    path('admin/', AdminOnlyView.as_view(), name='admin'),
    path('user/', UserOnlyView.as_view(), name='user'),
    path('adminOrSuperAdmin/', AdminOrSupperAdminOnlyView.as_view(), name='adminSuperAdmin'),
]