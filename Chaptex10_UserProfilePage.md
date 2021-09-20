# User Profile

- We prepare a profile page for users
- Decorate the page with the bootstrap

## Add a Profile Edit page for User

- We add a html page \members\templates\registration\profileedit.html
- we add a new view in \members\views.py

```html
<!--a profileedit.html pahe-->
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Profile </title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Profile</h1>
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Update Profile</button>
  </form>
</div>

{% endblock%}

```
views.py
```python
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm
# 1 User Registration
class UserRegisterView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#2 For User Profile edit
class UserEditView(generic.UpdateView):
    #form_class = UserCreationForm
    form_class = UserChangeForm
    template_name = 'registration/profileedit.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user
```
urls.py
```python
from django.urls import path 
from .views import UserRegisterView, UserEditView
#members views/urls here
urlpatterns = [
    path('members/',UserRegisterView.as_view(), name = 'register'),
    path('members/profile/',UserEditView.as_view(), name = 'editprofile'),
]
```
Now we add url to the navbar
```html
<ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="{% url 'editprofile' %}">Profile</a></li>
            <li><a class="dropdown-item" href="#">Setting</a></li>
            <li><hr class="dropdown-divider" /></li>
            <li>
              <a class="dropdown-item" href="{% url 'logout' %}">Logout</a>
            </li>
          </ul>
```
## Add Bootstrap the the Profile page
- We start with the form name EditProfileForm, that we add it in a forms.py of members
- EditProfileForm inherits UserChangeForm
```python

#Edit Profile Form
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User name'}))
    last_login = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last login'}))
    is_supperuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField( widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField( widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password','last_login', 'is_supperuser','is_staff','is_active','date_joined')
```
Then we modify the views.py of members
```python
#2 For User Profile edit
class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/profileedit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
```
## Change Password
- We add a new path in the urls.py of members. The path of django auth views
- This is simple way, but users will go to the django admin view
```python
from django.urls import path 
from .views import UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('profile/',UserEditView.as_view(), name = 'editprofile'),
    path('password/',auth_views.PasswordChangeView.as_view(), name = 'changepassword'),
]
```
- We will use our custom page to change password
- We will add a new page, the changepassword.html in the templates\registration\
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Change Password</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Change Password</h1>
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Change Password</button>
  </form>
</div>

{% endblock%}
```
- Then we adjust the urls.py 
```python
from django.urls import path 
from .views import UserRegisterView, UserEditView,BlogAppPasswordChangeView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name = 'register'),
    path('profile/',UserEditView.as_view(), name = 'editprofile'),
    #path('password/',auth_views.PasswordChangeView.as_view(), name = 'changepassword'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
    path('password/',BlogAppPasswordChangeView.as_view(template_name = 'registration\changepassword.html'), name = 'changepassword'),
]
```
## Change Password if OK then show an inform page
- If we want to show the page that inform the user has changed the password successfully, we we add a new template and  view
```html
<!-- passwordchangedsuccess.html -->
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Password updated</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Password changed successfully</h1>
{% endblock%}

```
we add a def view to use this template
```python
#3 Change password
class BlogAppPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('passwordchangedsuccess')

#4 Password sucess
def PasswordChangedSuccessView(request):
    return render(request, 'registration/passwordchangedsuccess.html', {})
```
We update the paths for urls.py
```python
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
```
## Add bootstrap for the Change Password
- We add a BlogPasswordChangeForm for that. To know which field names for the widget , you can view the html source of the PasswordChangeForm
```python
#Custome form for registragion
class BlogPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2= forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')
```
We will use this form for the view BlogAppPasswordChangeView
```python
#3 Change password
class BlogAppPasswordChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = BlogPasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('passwordchangedsuccess')
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
