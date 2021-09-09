# djangoblog 
This is a simple blog that developed based on django='3.1.3' and bootstrap4
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
## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)
