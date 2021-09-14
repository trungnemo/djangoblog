from django.urls import path 
from .views import UserRegisterView
#members views/urls here
urlpatterns = [
    path('members/',UserRegisterView.as_view(), name = 'register'),
]