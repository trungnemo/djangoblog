# Add a new blog
We will prepare all the things to show a blogadd page, for user to add a new one and save the blog into the database
- We add a new class BlogAddView that inherit Django.view.generic CreateView
- We prepare a blogadd.html 
- We modify the models.py and urls.py

Then here wwe go

## BlogAddView 
to add a new function for url for adding a new post

We update the views.py as
```python
#We use the Class View as follow
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
#....
# Post Add to add a new post
class BlogAddView(CreateView):
    model = Post
    template_name = 'blogadd.html'
    # Soame specified fields in the form only
    # fields = ('title','title_tag', 'body','author')
    # All fields will appear in the form
    fields = '__all__'
```
We add a new page: blogadd.html in the templates folder
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Post Add</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Add a new Post</h1>
<!--Django Form to add a new post-->
<form method="POST">
  <!--Cross site for prevent any possible form hackings-->
  {% csrf_token %} 
  <!--django form: that comes with the Post model -->
  {{ form.as_p }}
  <button class="btn btn-primary">Submit</button>
</form>
{% endblock%}
```
Modify the models.py, urls.py
```python
#models.py to make the reverse url works after we click submit button to add a new post into db
#The page will comeback to the Newly added post in the BlogDetailView
from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse

#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)
    #That is a newly added codes for the reverse url
    def get_absolute_url(self):
        return reverse('blogdetail', args=(str(self.id)))
        # return reverse('home')

#The urls.py
from django.urls import path

from .views import HomeView, BlogDetailView, BlogAddView
urlpatterns = [
    #...newly added url
    path('blogadd/', BlogAddView.as_view(), name = "blogadd")
]
```
We update the 'BlogAddView' in the url link of the navigation
```html
<a class="nav-link" href="{% url 'blogadd' %}">New Post</a>
```
Now run the web Blog for testing
```bash
python manage.py runserver
```
## Style your blogadd form
From now we note, we use the django form as
- {{ form.as_p }} : this makes all the fields in the paragrap html tag
- {{ form.as_ul }} : this makes all the fields in the li - list itemt html tag
- {{ form.as_table }}: this make all the field in the column of the table 

So now, we use our customized form by add a new file forms.py into the blog
```python
from django import forms
from .models import Post 

#Customized form for the Post model
from django import forms
from .models import Post 

#Customized form for the Post model
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'})
        }
```
Cause , each input fields in the class PostForm, 
We use the class="form-control" from bootstrap, we adjust the blogadd.html , where hosts the form
```html
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

<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Submit</button>
  </form>
</div>

{% endblock%}
```
Now, we use the PostForm 
```python
#Add the custom PostForm into the views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
#Use the customized form
from .forms import PostForm
#.....other defs

# Modify the BlogAddView to use the custom form: PostForm
class BlogAddView(CreateView):
    model = Post
    #Just Add this to use the custom form
    #and remove the fields = (cause the PostForm take care all of the fields)
    form_class = PostForm 
    template_name = 'blogadd.html'   
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

