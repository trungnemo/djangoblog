# Edit a Blog post
We are going to edit/delete a post from the list we added before
- We prepare a blogedit.html
- We modify the views.py by add the function for edit that firstly inherit the Django UpdateView 
- We modify the models.py and urls.py

Then here we go
## blogedit.html
To add a html page into the templates folder, it is blogedit.html.
The version dese not use form
```html
{% extends 'base.html' %}
<!--Title-->
{% block title%}
<title>Blog Edit Page</title>
{% endblock %}
<!-- Content-->
{% block content%}
<div class="container">
  <h3 class="mt-5 text-center">Edit a post</h3>
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-secondary">Submit</button>
  </form>
</div>
{% endblock %}
```
## Function for edit a post in views.py
```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
#Use the customized form
from .forms import PostForm
#...other def

# View to edit a post
class BlogEditView(UpdateView):
    model = Post
    template_name = 'blogedit.html'
    fields = ['title', 'title_tag', 'body']

#Now come urls.py, to add a new url path for the this BlogEditView
from django.urls import path
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit")
]
```
We add a link in a home page that contains a post list , a link will go to edit a selected post.
<a href="{% url 'blogedit' post.pk %}">Edit</a>
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
    <a href="{% url 'blogdetail' post.pk %}">{{ post.title }}</a> - {{
    post.author.first_name }} <a href="{% url 'blogedit' post.pk %}">Edit</a
    ><br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

## Upgrade by using the Customized form, by add the BlogEditForm, to the forms.py
```python
class PostEditForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'})
        }
#Then edit the view
class BlogEditView(UpdateView):
    model = Post
    template_name = 'blogedit.html'
    #Rem the fields of we use the Custom form
    #fields = ['title', 'title_tag', 'body']
    form_class = PostEditForm

```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

