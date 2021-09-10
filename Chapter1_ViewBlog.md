# View Blog
What we do here
- We will use the dashboard admin to input some data into the Blog table
- For the simplicity we will use the django.views.generic ListView and DetailView to Create views
- We use the home to as ListView
- We add a BlogDetail view

## Home page
Home view will list all the posts in the databae, we use inherit the ListView so we do not care about the SELECT query to list all the post.

We update the views.py as
```python
#We use the Class View as follow
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# #Home 1
# def home(request):
#     return render(request, 'home.html', {})
#Home view version 2
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
```
We update the home.html in the templates folder
```html
<h1>Posts</h1>
<ul>
  {% for post in object_list %}
  <li>
    <a href="{% url 'blogdetail' post.pk %}">{{ post.title }}</a> - {{
    post.author.first_name }} <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
```
We update the urls.py as
```python
from django.urls import path
#Home1
# from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetail
urlpatterns = [
    path('', HomeView.as_view(), name = "home")
]
```
## Blog Detail view
When we click the blog title, we will show the blogdetail.

We update the views.py as
```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#.....
class BlogDetail(DetailView):
    model = Post
    template_name = 'blogdetail.html'
```
We will create a blogdetail.html in the templates
```html
<h1>{{ post.title }}</h1>
<small>By: {{ post.author.first_name }} {{ post.author.last_name }} </small
><br />
<hr />
<br />
{{ post.body }}
<br />
<a href="{% url 'home' %}">Back</a>
```
We update the urls.py
```python
from django.urls import path
#Home1
# from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetail
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetail.as_view(), name = "blogdetail")
]

```
## Adding a Base html and and Bootstrap to our pages
Add the navigation.html in the template.

Then go to the getbootstrap.com, components, then copy the navbar with dropdown to the navigation.html
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```
Add a base.html in the templates folder of the blog'
[bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- copy the starter template
- paste it into the base.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU"
      crossorigin="anonymous"
    />

    <!--Block Title-->
    {% block title%} {% endblock %}
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"
      crossorigin="anonymous"
    ></script>
     <!--Navbar-->
    {% include 'navigation.html' %}
    <!--Block content-->
    <div class="container">
        {% block content%} {% endblock %}
    </div>
  </body>
</html>

```
Apply the base into the home.html
```python
{% extends 'base.html' %}
{% block title%}
    <title>The Block Home Page</title>
{% endblock%}
{% block content %}
<h1>Posts</h1>
<ul>
  {% for post in object_list %}
  <li>
    <a href="{% url 'blogdetail' post.pk %}">{{ post.title }}</a> - {{
    post.author.first_name }} <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

