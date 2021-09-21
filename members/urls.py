from django.urls import path 
from .views import UserRegisterView, UserEditView,BlogAppPasswordChangeView, PasswordChangedSuccessView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('profile/',UserEditView.as_view(), name = 'editprofile'),
    #path('password/',auth_views.PasswordChangeView.as_view(), name = 'changepassword'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
    path('password/',BlogAppPasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
    path('password/changed_success',PasswordChangedSuccessView, name = 'passwordchangedsuccess'),
]