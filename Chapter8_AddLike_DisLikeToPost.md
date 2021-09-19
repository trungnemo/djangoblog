# Add Likes to a Post
- We learn ManyToManyField in the model
- We learn how to add a SINGLE form submit button
- We lear new method: get_object_or_404
- We learn to add the view that update the ManyToMany value, and redirect to the same page
## Modify the Post model
- we add a new field to a Post model, a fields of ManyToManyField
- ManyToManyField:one post can be like by MANY users, and a USER can like MANY posts , so we have many to many relationship of Likes between USERS and POSTs
- Here we go to modify the models.py
```python
#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
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
        # return reverse('home')
```
Then we migrate to the db
```bash
python manage.py makemigartions
python manage.py migrate
#We can run the python manage.py dbshell to check what changes did we do to the sqllite db
```
- Run python manage.py dbshell to show the db information
- Window, if error with dbshell then download the  command-line shell tools and update PATH for Window, if Linux then run sudo apt-get install sqlite3 libsqlite3-dev
```bash
#Show the list of tables
sqlite> .tables
#Show the table columns / fields
.header on
.mode column
pragma table_info('blog_post_likes');
select * from blog_post_likes;
```

## Add Like buttons to blogdatail.html
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
<!-- To keep the html tag in the body we add !safe -->
<!-- |safe -->
{{ post.body |safe }}
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">Back</a>
<!--Add the Form like_blogpost with the button like-->
<br/>
<hr>
<form action="{% url 'like_blogpost' post.pk %}" method = "POST">
    {% csrf_token %}
    <button type = "submit", name = "like_post_id", value = "{{ post.id }}" , class = "btn btn-primary btn-sm" >
        Like
    </button>
</form>
{% endblock%}
```
## Add def BlogPostLikeView  into views.py
We add the BlogPostLikeView in the views.py , for this view we use , get_object_or_404 and  HttpResponseRedirect
```python
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
#Use the customized form
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
#....we import get_object_or_404, HttpResponseRedirect,reverse 
#...others views
#Like view
def BlogPostLikeView(request, pk):
    #like_post_id is the name of the button we add in the blogdetail.html
    post = get_object_or_404(Post, id = request.POST.get('like_post_id'))
    #Sabe the post likes, we do not save the post, we sabe post likes
    post.likes.add(request.user)
    #After likes, we stay on the same page: the Post page, so we do
    # we redirect to the blogdetail with the id that we have in here the pk
    return HttpResponseRedirect(reverse('blogdetail', args = [str(pk)]))
```
## We add a new path to the urls.py
We add the urls.py with the new views
```python
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView, BlogDeleteView,CategoryAddView,CategoryPostsView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit"),
    path('blogdelete/<int:pk>', BlogDeleteView.as_view(), name = "blogdelete"),
    path('categoryadd/', CategoryAddView.as_view(), name = "categoryadd"),
    path('categoryposts/<str:cats>/', CategoryPostsView, name = "categoryposts"),
    path('blogpostlike/<int:pk>/', BlogPostLikeView, name = "like_blogpost"),
]
```
## Add like count into the blogdetail page
- We add the function in the model to return the total like for a post
- We modify the BlogDetailView to get the total_like in the context
```python
# Detail Post
#We add the function total_likes to the Post model
def total_likes(self):
    # return how many users likes (records in the table blogpost_likes for this post id only)
    return self.likes.count()


#view
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogdetail.html'
    
     # Add Category to navbar
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        # Get the post and then get the like count for the post
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context
```
- Then we add the like count  into the blogdetail page. That is {{ total-likes }}
```html
<!--Add the Form like_blogpost with the button like-->
<br/>
<hr>
<form action="{% url 'like_blogpost' post.pk %}" method = "POST">
    {% csrf_token %}
    <button type = "submit", name = "like_post_id", value = "{{ post.id }}" , class = "btn btn-primary btn-sm" >
        Like - {{ total-likes }}
    </button>
</form>
```
# Add UnLike to a Post
- When a logon user already likes this post, the title button  will be Unlike, otherwize, title will be like
- When click LIKE, app will add one more like, otherwise remove the like.
 
So we start with the views.py
## View for unlike
```python
#Like view
def BlogPostLikeView(request, pk):
    #like_post_id is the name of the button we add in the blogdetail.html
    post = get_object_or_404(Post, id = request.POST.get('like_post_id'))
    liked = False #request.user does not like the post yet, True already liked this post
    #Adjust the rules: for LIKE and UNLIKE
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    #After likes, we stay on the same page: the Post page, so we do
    # we redirect to the blogdetail with the id that we have in here the pk
    return HttpResponseRedirect(reverse('blogdetail', args = [str(pk)]))

#the Detail view, add more context to specify LIKED or NOT LIKE yet

# Detail Post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogdetail.html'
    
     # Add Category to navbar
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        # Get the post and then get the like count for the post
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
         #the logon user Liked already yet
        liked = False 
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
         
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
```
Now we update the blogdetail to reflect the like and unlike button 
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
<!-- To keep the html tag in the body we add !safe -->
<!-- |safe -->
{{ post.body |safe }}
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">Back</a>
<!--Add the Form like_blogpost with the button like-->
<br />
<hr />
<form action="{% url 'like_blogpost' post.pk %}" method="POST">
  {% csrf_token %}
  <!--Check if Like or Unlike based on the context liked-->
  {% if user.is_authenticated %} {% if liked %}
  <button
    type="submit"
    ,
    name="like_post_id"
    ,
    value="{{ post.id }}"
    ,
    class="btn btn-danger btn-sm"
  >
    UnLike - ({{ total_likes }} Likes)
  </button>
  {% else %}
  <button
    type="submit"
    ,
    name="like_post_id"
    ,
    value="{{ post.id }}"
    ,
    class="btn btn-primary btn-sm"
  >
    Like
  </button>
  {% endif %} {% else %}
  <a href="{% url 'login' %}">Login</a> to like {% endif%} - ({{ total_likes }}
  Likes)
</form>
{% endblock%}

```


## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
