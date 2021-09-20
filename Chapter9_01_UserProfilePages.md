# User Profile

- We prepare a profile page for users

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

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
