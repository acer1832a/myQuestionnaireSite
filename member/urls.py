from django.urls import path

from . import views

app_name = 'member'

urlpatterns = [
    path('', views.index.as_view() , name='index'),
    path('register/', views.register.as_view() , name='register'),
    path('login/', views.user_login.as_view(), name='user_login'),
    path('logout/', views.user_logout.as_view(), name='logout'),
]