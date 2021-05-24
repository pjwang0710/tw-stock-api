from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('get_users/', views.get_users, name='get users'),
    path('get_user_detail/<str:pk>/', views.get_user_detail, name='get user detail'),
    path('insert_user/', views.insert_user, name='insert user'),
    path('login/', views.login, name='login'),
    path('update_user/<str:pk>', views.update_user, name='update user'),
    path('delete_user/<str:pk>', views.delete_user, name='delete user')
]
