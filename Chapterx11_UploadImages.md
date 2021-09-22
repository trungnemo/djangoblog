# Upload Images

- We add, modify the models/DB Tables to keep the image data

## Model Image field
- Modify the Post model
```python
#We add this to the Class Post
    #image field: Allow null,Accept empty input, if any image upload to the folder images/
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
```
- We make migrations after model changes
```bash
#We have to install the Python image library before make migrations
python -m pip install Pillow
#Then we make migrations
python manage.py makemigrations
python manage.py migrate
```
Now we make some changes 
- Add <form method="POST" enctype="multipart/form-data"> to the blogadd.html, so let the form accepts the image field data
- Add header_image to the fields in the forms.py
blogadd.html
```html
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST" enctype="multipart/form-data">
    {% csrf_token %} {{ form.media }} {{ form.as_p }}
    <button class="btn btn-primary">Submit</button>
  </form>
</div>
```
forms.py
```python
fields = ('title', 'title_tag', 'author', 'category','body', 'snippet','header_image')
```
- We add the MEDIA_URL into the settings.py of the djangoblog broject
```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#...others
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')
)
#Then we go to the urls.py of members to import these settings before using in the image upload
from django.contrib import admin
from django.urls import path, include
#for the image update settings
from django.conf import settings
from django.conf.url.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
- Now try to add some new posts with header_iamges uploaded
- Then we add the headers images in the blogdetail.html
```html
<!--Add this in the blogdetail.html before the {{ post.body | safe }}-->
<img src="{{ post.header_image.url  }}" alt="">
{{ post.body |safe }}
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)

## License
[MIT](https://choosealicense.com/licenses/mit/)
