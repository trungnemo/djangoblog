from django.urls import path 
from .views import UserRegisterView, UserEditView
#members views/urls here
urlpatterns = [
    path('members/',UserRegisterView.as_view(), name = 'register'),
    path('members/profile/',UserEditView.as_view(), name = 'editprofile'),
]