from django.db import models
from django.contrib.auth.models import User

#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)
