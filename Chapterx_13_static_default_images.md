# Default static profile image if not valid img url

- If user has not profile image then we load the default image in the STATIC instead
- Notes: 

django version before 3.1.0 , the setttings.py  there is an import os
but from after 3.1.0, no import os. So to avoid the error, we just add import os

## Put a default profile image into the static
We create a default a folder named static at the root of the project folder
```python
# The structure 
djangoblog
|-static
  |-css
  |-images
     - default-pic.png
  |-js
```
Now we update the settings.py of the project
```python

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
- Now we apply in navigation.html
- Note we will have to use {% load static %}
```html
<!--
            <img src="https://i.pravatar.cc/50" class="rounded-circle" />
            -->
            {% if user.profile.profile_pic  %}
              <img src="{{ user.profile.profile_pic.url }}" width="50"  height="50" class="rounded-circle" />
            {% else %} 
              <img src="{% static 'images/default_pic.png' %}" width="50"  height="50" class="rounded-circle" />
            {% endif %} 
            {{ user.username }}

```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)

## License
[MIT](https://choosealicense.com/licenses/mit/)
