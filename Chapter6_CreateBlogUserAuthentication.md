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
Now we update the navigation.html 
- if a User is authenticated then will display the logout and hide the login and register links
- we load the user information
The build in django function wwe will use is: user.is_authenticated
We will do the same thing for the html page to hide the edit and delete links
```html 
   {% if user.is_authenticated %}
      <ul class="navbar-nav">
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdown"
            role="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <img
              src="https://i.pravatar.cc/50"             
              class="rounded-circle"
            />
            {{ user.username }}
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><a class="dropdown-item" href="#">Setting</a></li>
            <li><hr class="dropdown-divider" /></li>
            <li>
              <a class="dropdown-item" href="{% url 'logout' %}}">Logout</a>
            </li>
          </ul>
        </li>
      </ul>
      {% endif %}

```
Upto now we can bypass the check of user.is_authenticated form the home page, by go directly to the links of
- Add a new blog: http://127.0.0.1:8000/blogadd/
- A blog detail : http://127.0.0.1:8000/blog/2
If we by pass it, we can still add , edit or delete a blog without authentication.
So we can do by adding the check {% user.isauthenticated %} on each page like that
```html
<!-- what we do for blogadd.html -- >
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Post Add</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Add a new Post</h1>
<!-- Version of Django Form no Bootstrap

<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button class="btn btn-primary">Submit</button>
</form>

end of first version -->

{% if user.is_authenticated %}
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Submit</button>
  </form>
</div>
{% else %}
<p>You are not authiticated to go on more...!</p>
{% endif %}

{% endblock%}
```


## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

