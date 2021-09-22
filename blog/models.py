from django.db import models
from django.contrib.auth.models import User
# Add this import for the add a new post 
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
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
    #body = models.TextField()
    body = RichTextField(blank = True, null = True)
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default="None")
    snippet = models.CharField(max_length=255, default="Click link above to read full text")
    #ManyToMany Likes relations ships
    likes = models.ManyToManyField(User, related_name="users_like_posts")
    #image field
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")

    def total_likes(self):
        # return how many users likes (records in the table blogpost_likes for this post id only)
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse('blogdetail', args=(str(self.id)))
        return reverse('home')

# User Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profiles/")
    website_url = models.CharField(max_length=255, null = True, blank = True)
    facebook_url = models.CharField(max_length=255, null = True, blank = True)
    twitter_url = models.CharField(max_length=255, null = True, blank = True)
    instagram_url = models.CharField(max_length=255, null = True, blank = True)
    pinterest_url = models.CharField(max_length=255, null = True, blank = True)

    def __str__(self):
        return str(self.user)