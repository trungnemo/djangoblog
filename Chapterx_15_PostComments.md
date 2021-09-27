# Comments
- Build a function to let the logon user to comment on posts
## Comment Model
- Add a Class model to the models.py in the blog app
```python
class Comment(models.Model):
    #The relation: many comment for one post , one a post is delete then all comments for that posts will be deleted too
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #The name of user who did make comment on the post
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
```
- Migrate the new model to the DB structure
```bash
python manage.py makemigrations
python manage.py migrate
```
- Now we register this comment model to the django dashboard amdin
```python
from django.contrib import admin
from .models import Post , Category, Profile, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
```
- We use the dashboard admin to add some comment to have the data for testing
## Show comments on a Blog post detail page
- We modify the blogdetails.html ,... to show the comments for the post
- Notes how to get comments of a post
```python
#remeber the: related_name="comments", so 
{% if not post.comments.all %} -> CHeck IF NOT COMMENT
```
- Now add comments to be shown on the blogdetail.html
```html
<!--Add these after the like form -->
<!--Comments-->
<br/>
<hr/>
<h2>Comments</h2>
<br/>
{% if not post.commetns.all %}
  <p>No comments...! <a href="">Add Comments</a></p>
{% else %}
  {% for comment in post.comments.all %}
    <strong>{{ comment.name }}</strong>
    <br/>
    {{ comment.body }}
    <br/>
    <br/>
  {% endfor %}
{% endif %}
```
## Add comments on a post
- Add a class view
```python
# Comment Views
class CommentAddView(CreateView):
    model = Comment
    template_name = 'comment_add.html'
    fields = '__all__'
```
- Add a page in to the templates: comment_add.html
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Add Comment</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Add My comment</h1>

{% if user.is_authenticated %}
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Submit</button>
  </form>
</div>

{% else %}
<p>You are not authenticated to go on more...!</p>
{% endif %} {% endblock%}

```
- Add a page for the CommentAddView to the urls.py
```python
from django.urls import path
from . import views



# urlpatterns = [
#     path('', views.home, name = "home")
# ]
from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView, BlogDeleteView,CategoryAddView,CategoryPostsView, BlogPostLikeView, CommentAddView
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blogdetail"),
    path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    path('blogedit/<int:pk>', BlogEditView.as_view(), name = "blogedit"),
    path('blogdelete/<int:pk>', BlogDeleteView.as_view(), name = "blogdelete"),
    path('categoryadd/', CategoryAddView.as_view(), name = "categoryadd"),
    path('categoryposts/<str:cats>/', CategoryPostsView, name = "categoryposts"),
    path('blogpostlike/<int:pk>/', BlogPostLikeView, name = "like_blogpost"),
    path('blog/<int:pk>/addcomment', CommentAddView.as_view(), name = "addcomment"),
]
```
- Add this url in the bloddetail.html
```html
<h2>Comments</h2>
<br/>
<a href="{% url 'addcomment' post.pk %}">Add Comments</a></p>
{% if post.comments.all %}
   {% for comment in post.comments.all %}
    <strong>{{ comment.name }}</strong>
    <br/>
    {{ comment.body }}
    <br/>
    <br/>
  {% endfor %}
{% endif %}

```
- We add a CommentAddForm into forms.py add a comment
```python
class CommentAddForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Comment 
        fields = ('name', 'body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'User name '}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'}),
         }

#we modifify the view(add from_class, rem fields)
# Comment Views
# Comment Views
#CommentAddView_Noform
# class CommentAddView(CreateView):
#     model = Comment
#     template_name = 'comment_add.html'
#     fields = '__all__'
#     success_url = reverse_lazy('home')

# CommentAddView With Form
class CommentAddView(CreateView):
    model = Comment
    template_name = 'comment_add.html'
    #fields = '__all__'
    form_class = CommentAddForm

    def form_valid(self, form):
        #We can run CommentAddView noform then go to developer view, to get this field
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

```

## Contributing
[TrungNemo](https://www.facebook.com/TrungNEMO)
## License
[MIT](https://choosealicense.com/licenses/mit/)
