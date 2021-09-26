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



## Contributing
[TrungNemo](https://www.facebook.com/TrungNEMO)
## License
[MIT](https://choosealicense.com/licenses/mit/)
