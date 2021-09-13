# Create a blog user authentication
Upto now, everydo can go the out web, add a post and event edit, delete the posts that are not created by them.It is not right. So we will tight it up form here, with
## Create members django app
- User authentication: a user must register an account, to logon the blog for blog posting
We start by adding a new django app named 'members', this app will specifically care about user members
```bash
python manage.py startapp members
#This project has all the files pre-created by django just like blog, but no urls.py
#we add urls.py to the members folder.
```
The newly addded urls.py
```python
from django.urls import path 
#members views/urls here
urlpatterns = [

]
```
Go to the settings of the django project to add this app
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'members'
]
```
Edit the urls.py of the blog like this
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # this added for members app with predefined auth form django
    path('members', include('django.contrib.auth.urls')),
    path('members', include('members.urls')),
]
```
## Template html pages for authentication
Then now here we go develop the authentication with
- Registration page
- Login page
We create the html pages for the templates by
- We will create a templates folder in the members app
- We add a sub registration folder in the templates
- We add login.html and registration.html in the .\templates\registration\ (We do not need page for a logout)
```html
```
## views.py of members app for urls
```python
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# 1 User Registration
class UserRegisterView(generic.CreateView):
    form_class = UserCreationFormt
    template_name = 'registration/register.html'
    success_ulr = reverse_lazy('login')
```
## urls.py of members app that goes with the view definitions
```python
from django.urls import path 
#members views/urls here
urlpatterns = [
   path('register/',UserRegisterView.as_view(), name = 'register'),
]
```
## Wrap up
We add the link in the navigation to go to the register page
```html
<nav>
<!-- .. -->
     <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'home' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'blogadd' %}">New Post</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'register' %}">Register</a>
        </li>
      </ul>

</nav>
```
Add the followings settings into the settings.py of the djangoblog (django project folder)
```python
#Add the default redirect for login and logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

