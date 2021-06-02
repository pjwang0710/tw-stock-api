from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('get_users', views.get_users, name='get_users'),
    path('get_user_detail/<str:pk>', views.get_user_detail, name='get_user_detail'),
    path('insert_user', views.insert_user, name='insert_user'),
    path('login', views.login, name='user_login'),
    path('update_user/<str:pk>', views.update_user, name='update_user'),
    path('delete_user/<str:pk>', views.delete_user, name='delete_user'),
    path('update_secret_key/<str:pk>', views.update_user_secret, name='update_secret_key'),
    path('get_secret_key/<str:pk>', views.get_secret_key_detail, name='get_secret_key')
]
