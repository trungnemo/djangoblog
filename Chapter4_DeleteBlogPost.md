# Delete a Blog post
We are going to delete a post from the list we added before, we will do
- Add a blogdelete.html
- Add a def BlogDeleteView in a views.py
- Add a url to a urls.py

Here we go with the view
## views.py
```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
#Use the customized form
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy
#...other defs

# To Delete a post
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogdelete.html'
    # After a post is deleted, it will be redrected to home page, 
    # Delete use this method, nos as BlogEditView with get_absolute_url in the models
    success_url = reverse_lazy('home')
   
```
Herea we go with the blogdelete.html
## templates\blogdelete.html
```html
{% extends 'base.html' %}
<!--Title-->
{% block title %}
<title>Delete a Post</title>
{% endblock %}

<!--Content-->
{% block content %}
<h1 class="mt-5 text-center">Delete a Post</h1>
<h3 class="mt-5 text-center">{{ post.title }}</h3>
<br />
<div class="form-group">
  <form method="POST">
    {% csrf_token %}
    <!--Confirmation button : Later can be raplace by a model -->
    <strong>Are you sure, to delete this post!?</strong>
    <button class="btn btn-danger">Delete it</button>
  </form>
</div>
{% endblock %}
```
Add a url in the urls.py
```python
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit"),
    path('blogdelete/<int:pk>', BlogDeleteView.as_view(), name = "blogdelete"),
]
```
Add a delete link in the Blog post list in a home page
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Block Home Page</title>
{% endblock%}
<!--Content Page-->
{% block content %}
<h1 class="mt-5 text-center">Posts</h1>
<ul>
  {% for post in object_list %}
  <li>
    <a href="{% url 'blogdetail' post.pk %}">{{ post.title }}</a> -
    <small><a href="{% url 'blogedit' post.pk %}">(Edit)</a></small> - 
    <small><a href="{% url 'blogdelete' post.pk %}">(Delete)</a></small>
    <br />
    {{post.author.first_name }} {{ post.author.last_name }}
    <br />
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

