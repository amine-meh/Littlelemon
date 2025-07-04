from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.index, name='index'),
  path('menu-items/', views.MenuItemView.as_view(), name="MenuItems"),
  path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name="MenuItem"),
  path('auth-token/', obtain_auth_token),
]