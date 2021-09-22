# Upgrade User Profile with Cover photo

- Add new model name Profile


## model.py
We add a new model named Profile in the blog\models.py
```python
# User Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
```
- Migrate the models to the DB structures
```bash
python manage.py makemigrations
python manage.py migrate
```
- Register Profile to the django Dashboard admin.py
```python
from django.contrib import admin
from .models import Post , Category, Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
```
- Now we run the server, go to the http://127.0.0.1:8080/admin to update some bios
- The add the bio to the profileedit.htmo in members\templates
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Profile</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Profile</h1>
<br />
{{ user.profile.bio }}
<br />
<hr />
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Update Profile</button>
  </form>
</div>

{% endblock%}
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)

## License
[MIT](https://choosealicense.com/licenses/mit/)
