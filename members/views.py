from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, BlogPasswordChangeForm

# 1 User Registration
class UserRegisterView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#2 For User Profile edit
class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/profileedit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

#3 Change password
class BlogAppPasswordChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = BlogPasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('passwordchangedsuccess')

#4 Password sucess
def PasswordChangedSuccessView(request):
    return render(request, 'registration/passwordchangedsuccess.html', {})