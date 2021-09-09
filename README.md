# djangoblog 
This is a simple blog that developed based on django='3.1.3' and bootstrap4
This codes based from the following tutorials
- [Simple Blog By Codemy.com](https://www.youtube.com/watch?v=CnaB4Nb0-R8&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=2)
- [Photo Album App by Dennis Ivy](https://www.youtube.com/watch?v=sSquD2u5Ie0)
## Start-up
```bash
#Create a virtual evironment
python -m venv venv_quickdjango
pip install django=3.1.3
#Create a django project
django-admin startproject djangoblog
#Migrate the admin db dashboard
python manage.py migrate
#Create a super user admin
python manage.py createsuperuser
#Create django app: blog
python manage.py startapp blog
#add blog the settings.py in the djangoblog
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
#Add the urls.py to the blog folder
#Add the following codes to the urls.py in the djangblog
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
#Add a home function to the views.py of the blog
def home(request):
    return render(request, 'home.html', {})
```
Add the home.html to
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Blog</title>
</head>
<body>
    <h1>The simple blog will be here</h1>
</body>
</html>
```
## Post Model for DB
Declare the Post class in the models.py for the Post table in the DB
```python
from django.db import models
from django.contrib.auth.models import User

#Post class for the post table in the db
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + self.author

#register the Post in the Django admin dashboard,in the admin.py of blog
from django.contrib import admin
from .models import Post 
# Register your models here.
admin.site.register(Post)
```
After define the model, then migrate the Class into the DB
```bash
python manage.py makemigrations
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)
