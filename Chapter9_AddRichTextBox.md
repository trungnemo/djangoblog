# Add a RichTextBox editor to the Blog

- We are going to add CKEditor to the blog for the Blog description field

## Installation

```bash
pip install django-ckeditor
```
We add the app to the INSTALL APSP in settings of the djangoblog folder (the project)
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
    'members',
    'ckeditor'
]
```
## Edit the models.py
- First we import for usage: from ckeditor.fields import RichTechField
- We declare the body field as: body = RichTechField(...)
```python
from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTechField
#....
#Post class for the post table in the db
from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
#...
#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank = True, null = True)
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default="None")
    #ManyToMany Likes relations ships
    likes = models.ManyToManyField(User, related_name="users_like_posts")

    def total_likes(self):
        # return how many users likes (records in the table blogpost_likes for this post id only)
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('blogdetail', args=(str(self.id)))
```
We change the model then we make the migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
- Now we can test, by running the server, and go the dashboard admin, to edit a blog. we will see it works in the dashboard. But not for the our pages: Add new and edit a blog.
- We will now modify the blogadd, blogedit.html in the templates, we add  {{ form.media }} {{ form.as_p }}
- Remember we use the safe for the {{ post.body | safe}} for keeping the format tags
```html
{% extends 'base.html' %}
<!--Title-->
{% block title%}
<title>Blog Edit Page</title>
{% endblock %}
<!-- Content-->
{% block content%}
<div class="container">
  {% if user.is_authenticated and user.id == post.author.id %}
  <h3 class="mt-5 text-center">Edit a post</h3>
  <form method="POST">
    {% csrf_token %} {{ form.media }} {{ form.as_p }}
    <button class="btn btn-secondary">Submit</button>
  </form>
  {% else %}
  <p>Page not found 404</p>
  {% endif %}
</div>
{% endblock %}

```
# Add a snippet to a blog post
## Add snippet field to Post model
```python
#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    #....
    snippet = models.CharField(max_length=255, default="Click link above to read full text")
```
After change the model, we make migrations to the DB
```bash
python manage.py makemigrations
python manage.py migrate
```
We show the post snippet in the home page
```
...
    {{ post.snippet }}
    <!-- just show first 200 chars of Body -->
    <!-- We add |safe to tell django does not remove the html tag in the body text of the blog-->
    <!-- {{ post.body | slice:":200" |safe}} -->
```
We add snippet field in to the blog add and edit page by modifying the forms.py
```python
#Customized form for the Post model
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category','body', 'snippet')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authorid', 'type':'hidden'}),
            # 'category': forms.Select(choices = choices, attrs={'class':'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'}),
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Post snippet'})
        }

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
