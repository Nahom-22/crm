from django.urls import path
from . import views


extraurlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.home, name=''),

]