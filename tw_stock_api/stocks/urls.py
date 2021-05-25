from django.urls import path

from . import views

urlpatterns = [
    path('get_stock_info/<str:pk>/<str:secret_key>', views.get_stock_info, name='get_stock_info'),
    path('get_api_user_count/<str:pk>', views.get_api_user_count, name='get_api_user_count')
]
