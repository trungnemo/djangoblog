# Blog categories
Now we want to add the categories to our blog post, example Sports, Dancing, Programing...
## First thing first, Category model
We add a category model to the models.py in the blog 
```python
from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse
from datetime import datetime, date
#Post Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')
#Add new field to the Post model
category = models.CharField(max_length=255, default="None")
```
next we migrate the new model to the DB
```bash
python manage.py makemigrations
python migrate
```
then we register the Category model into the django dashboard, add the codes to the admin.py
```python
from django.contrib import admin
from .models import Post , Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
#Then goto the http://127.0.0.1:8000/admin/blog/category/
#Add some categories such as Programming, Sports, Movies
```
## Add category field of Post to the Blog Add, Edit form
We hardcode to simulate ho the category data will be loaded into the Category select of the form.
We use the variables choices, the data type is list of turple
```python
from django import forms
from .models import Post 

#Temp data to simulate the category select form control
#We define the data type list of turple
choices = [('Sport','Sport'), ('Music','Music'), ('Reading','Reading')]

#Customized form for the Post model 
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', ,'category','body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            #Temp add the form for add a new blog post
            'category': forms.Select(choices = choices, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'})
        }
```
Now we get the categories from DB 
```python
from django import forms
from .models import Post , Category

#Temp data to simulate the category select form control
#We define the data type list of turple

#choices = [('Sport','Sport'), ('Music','Music'), ('Reading','Reading')]

choices = Category.objects.all().values_list('name','name')
choice_list = []
for c in choices:
    choice_list.append(c)

#Customized form for the Post model
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category','body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            # 'category': forms.Select(choices = choices, attrs={'class':'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'})
        }

```

## Create a page to add a new category to the database
We start by add a categoryadd.html.
We copy the blogadd.html and past it into the category.html
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Add a new category</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Add a new category</h1>

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
Add CategoryAddView class into the views.py
```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
#Use the customized form
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy
#...other defs
# Category views
class CategoryAddVoew(CreateView):
    model = Category
    template_name = 'categoryadd.html'
    fields = '__all__'
```
We add CategoryAddView to the urls.py
```python
from django.urls import path
from . import views

from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView, BlogDeleteView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    #...other urls
    path('categoryadd/', CategoryAddView BlogDeleteView.as_view(), name = "categoryadd"),
]
```
We add a link to the navagation.html to go to the categoryadd.html
```html
 {% if user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'blogadd' %}">New Post</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'categoryadd' %}">New Category</a>
        </li>
 {% else %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'register' %}">Register</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'login' %}">Login</a>
        </li>
 {% endif %}
```
## Filter posts by clicking on a Category in a home page
We add a new view into a views.py, this time, we use the function view
```python
#CategoryPostsView: List all posts by category
def CategoryPostsView(request, cats):
    #cats is the paramters passed in for filter all posts  of category
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categoryposts.html', {'cats':cats,'category_posts':category_posts})
```
We add a new path into an urls.py
```python
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView, BlogDeleteView,CategoryAddView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit"),
    path('blogdelete/<int:pk>', BlogDeleteView.as_view(), name = "blogdelete"),
    path('categoryadd/', CategoryAddView.as_view(), name = "categoryadd"),
    #This path
    path('categoryposts/<str:cats>/', CategoryPostsView.as_view(), name = "categoryposts"),
]
```
We add a categoryposts.html into a templates
```htmls
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Posts by Category</title>
{% endblock%}
<!--Content Page-->
{% block content %}
<h1 class="mt-5 text-center">Posts of Category : {{ cats }}</h1>
<ul>
  {% for post in category_posts %}
  <li>
    <a href="{% url 'blogdetail' post.pk %}">{{ post.title }}</a> -
    <small>{{ post.category }}</small>
    {% if user.is_authenticated and user.id == post.author.id %}
    <small><a href="{% url 'blogedit' post.pk %}">(Edit)</a></small> -
    <small><a href="{% url 'blogdelete' post.pk %}">(Delete)</a></small>
    {% endif %}
    <br />
    {{post.author.first_name }} {{ post.author.last_name }}
    <small>{{ post.post_date }}</small>
    <br />
    <!-- 
        {{ post.body }}
        -->
    <!-- just show first 200 chars of Body -->
    <!-- We add |safe to tell django does not remove the html tag in the body text of the blog-->
    {{ post.body | slice:":200" |safe}}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```
Now we add a link to the category in the home page.
So when click to the category we will go to the categoryposts.html
```html
small><a href="{% url 'categoryposts' post.category %}"> {{ post.category }}</a></small>
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

