# How to add a new field to created Post Model
We are going to make some adjustment to the Post model
- Add new fields to Post Model
- Migrate a newly added fields to the DB
- Make some ordering based on the newly added field to the list on Home page

Here we go with the view
## models.py
We add a post_date with the datetime data type to the Post model
```python
from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse
from datetime import datetime, date
#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('blogdetail', args=(str(self.id)))
        # return reverse('home')
```
We migrate the changes to the DB
``` bash
python manage.py makemigrations
#When hit it, the following will come next, cause some posted already created before
You are trying to add the field 'post_date' with 'auto_now_add=True' to post without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
#we will go on with 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> timezone.now
#we will input timezone.now for all created posts, the the migration file we have
# Generated by Django 3.1.3 on 2021-09-12 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
```
Now we do migrate by running the generated script above
```bash
python manage.py migrate
```
We now, show the value of the added field to the blogdetail.html
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>{{ post.title_tag }}</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">{{ post.title }}</h1>
<small>By: {{ post.author.first_name }} {{ post.author.last_name }} </small>
<small>Date: {{ post.post_date }}</small>
<br />
<hr />
<br />
{{ post.body }}
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">Back</a>
{% endblock%}

```
Now we use the post_date for ordering the list
```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
#Use the customized form
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy
# #Home 1
# def home(request):
#     return render(request, 'home.html', {})

#Home view version 2
# List all Posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['id']: id order 1,2,3...n
    # ordering = ['-id']: id order n,..3,2,1
    # ordering = ['-id']
    ordering = ['-post_date']
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

