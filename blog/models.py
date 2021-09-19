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