from django.urls import path 
from .views import UserRegisterView
#members views/urls here
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name = 'register'),
]