from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('email-list', views.email_list, name='email-list'),
]
