# Create , Edit and View User Profile

Uptonow, we use the django dashboard admin to add, edit the Profile, now we do to add the following functionalities to maintain Profile
- Add
- Edit
- Display

## Display the User Profile
We start by adding UserProfileShowView into members\views.py
```python
#User extra profile

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

```
- We add a path to the urls.py with the profile id primary key as a parameters
```python
from django.urls import path 
from .views import UserRegisterView, UserEditView,BlogAppPasswordChangeView, PasswordChangedSuccessView, UserProfileShowView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
    #...,
    path('user_profile/<int:pk>',UserProfileShowView.as_view(), name = 'user_profile'),
    
]
```
- Add 'user_profile' url to the pages
- We add to the links on the home page to see the author profile
```html
<!-- Add the anchor to the home page so click the author and see the profile -->
<!-- But if user has no profile this will come up with error, we will fix it later-->
<a href="{% url 'user_profile' post.author.profile.id %}"> {{post.author.first_name }} {{ post.author.last_name }} </a> 

``` 
- Add add a new user_profile.html in the members\templates\registration\
```html
{% extends 'base.html' %}
{% load static %}

<!--Title page-->
{% block title%}
<title>User Profile</title>
{% endblock%}

<!--Title page-->
{% block content%}
<div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
        {% if user_profile.profile_pic  %}
            <img src="{{ user_profile.profile_pic.url }}" width="50"  height="50" class="rounded-circle" />
        {% else %} 
            <img src="{% static 'images/default_pic.png' %}" width="50"  height="50" class="rounded-circle" />
        {% endif %} 
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{{ user_profile }}</h5>
        {% if user_profile.bio %}
            <p class="card-text">{{ user_profile.bio }}</p>
        {% endif %} 
        <p class="text-muted">
          {% if user_profile.website_url %}
          <a href="{{ user_profile.website_url }}"> Website </a>| 
          {% endif %} 
          {% if user_profile.facebook_url %}
          <a href="{{ user_profile.facebook_url }}"> Facebook </a>| 
          {% endif %} 
          {% if user_profile.twitter_url %}
          <a href="{{ user_profile.twitter_url }}"> Twitter </a>| 
          {% endif %} 
          
          {% if user_profile.instagram_url %}
          <a href="{{ user_profile.instagram_url }}"> Instagram </a>| 
          {% endif %}

        </p>
      </div>
    </div>
  </div>
</div>

<a href="{% url 'home' %}" class="btn btn-secondary">Back</a>

{% endblock%}

```

## Edit User Profile
- Add a new UserProfileEditView  into the views.py
- Note for the {% if user.id == profile.user.id %}
```python
#User extra profile
class UserProfileEditView(generic.UpdateView):
    model = Profile
    template_name = 'registration/user_profile_edit.html'
    fields = ['bio', 'profile_pic', 'website_url','facebook_url','twitter_url','instagram_url','pinterest_url']
    success_url = reverse_lazy('home')
```
- Add a html to the members\templates\registration\user_profile_edit.html
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Profile Edit</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Edit Profile</h1>

{% if user.is_authenticated %}
    {% if user.id == profile.user.id %}

    <!--Customized form with bootstrap-->
    <div class="form-group">
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %} {{ form.media }} {{ form.as_p }}
        <button class="btn btn-primary">Save</button>
    </form>
    </div>

    {% else %}
         <p>You coult not edit the profile of the other...!</p>
    {% endif %}

{% else %}
    <p>You are not authiticated to go on more...!</p>
{% endif %} 

{% endblock%}

```

- Add a new page for UserProfileEditView  in the urls.py
```python
from django.urls import path 
from .views import UserRegisterView, UserEditView,BlogAppPasswordChangeView, PasswordChangedSuccessView, UserProfileShowView,UserProfileEditView
from django.contrib.auth import views as auth_views
#members views/urls here
urlpatterns = [
   #...,
    path('user_profile/<int:pk>',UserProfileShowView.as_view(), name = 'user_profile'),
    path('user_profile_edit/<int:pk>',UserProfileEditView.as_view(), name = 'user_profile_edit'),
    
]
```
- Now we add the links to go to Show, Edit Profile Pages in the navigation.html
```html
 <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="{% url 'registraion_edit' %}">Logon Info</a></li>
            {% if user.profile.id  %}
            <li><a class="dropdown-item" href="{% url 'user_profile' user.profile.id %}">Show Profile</a></li>
            <li><a class="dropdown-item" href="{% url 'user_profile_edit' user.profile.id %}">Edit Profile</a></li>
            {% else %}
            <li><a class="dropdown-item" href="{% url 'user_profile_create' %}">Create Profile</a></li>
            {% endif %}
            <li><hr class="dropdown-divider" /></li>
            <li>
              <a class="dropdown-item" href="{% url 'logout' %}">Logout</a>
            </li>
</ul>
```
## Create or Add a User Profile
-..
- ..
```python
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)

## License
[MIT](https://choosealicense.com/licenses/mit/)
