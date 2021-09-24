from django.urls import path 
from .views import UserRegisterView, UserEditView,BlogAppPasswordChangeView, PasswordChangedSuccessView, UserProfileShowView,UserProfileEditView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('profile/',UserEditView.as_view(), name = 'registraion_edit'),
    #path('password/',auth_views.PasswordChangeView.as_view(), name = 'changepassword'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
    path('password/',BlogAppPasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
    path('password/changed_success',PasswordChangedSuccessView, name = 'passwordchangedsuccess'),
    path('user_profile/<int:pk>',UserProfileShowView.as_view(), name = 'user_profile'),
    path('user_profile_edit/<int:pk>',UserProfileEditView.as_view(), name = 'user_profile_edit'),
    
]