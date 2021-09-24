from django.forms import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from blog.models import Profile

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
    template_name = 'registration/registraion_edit.html'
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

#User extra profile
class UserProfileShowView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

     # Add Category to navbar
    def get_context_data(self, *args, **kwargs):
        # profiles = Profile.objects.all()
        context = super(UserProfileShowView, self).get_context_data(*args, **kwargs)

        user_profile = get_object_or_404(Profile, id = self.kwargs['pk'])
        
        context["user_profile"] = user_profile
        return context


#User extra profile
class UserProfileEditView(generic.UpdateView):
    model = Profile
    template_name = 'registration/user_profile_edit.html'
    fields = ['bio', 'profile_pic', 'website_url','facebook_url','twitter_url','instagram_url','pinterest_url']
    success_url = reverse_lazy('home')