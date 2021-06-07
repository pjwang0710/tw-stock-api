from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('get_users', views.get_users, name='get_users'),
    path('get_user_detail', views.get_user_detail, name='get_user_detail'),
    path('insert_user', views.insert_user, name='insert_user'),
    path('login', views.login, name='user_login'),
    path('test_jwt', views.test_jwt, name='test_jwt'),
    path('update_user', views.update_user, name='update_user'),
    path('delete_user/<str:pk>', views.delete_user, name='delete_user'),
    path('update_secret_key', views.update_user_secret, name='update_secret_key'),
    path('get_secret_key', views.get_secret_key_detail, name='get_secret_key'),
    path('get_api_use_count', views.get_api_use_count, name='get_api_use_count')
]
