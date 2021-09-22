# Upgrade User Profile with Cover photo

- Add new model name Profile


## Add a bio text for the user Profile
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
## Add a profile pic and social links
- Start with the Profile model
```python
#Add this code to the class Profile in the models.py
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profiles/")
    #Add more
    website_url = models.CharField(max_length=255, null = True, blank = True)
    facebook_url = models.CharField(max_length=255, null = True, blank = True)
    twitter_url = models.CharField(max_length=255, null = True, blank = True)
    instagram_url = models.CharField(max_length=255, null = True, blank = True)
    pinterest_url = models.CharField(max_length=255, null = True, blank = True)
```
- Now run migrate
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
#goto admin dashboard to update the urls for a user
```
- We add these links to the blogdetail.html
- We go to the https://getbootstrap.com/docs/5.1/components/card/ ...then copy the Horizontal card 
```html
<!--User Profile img and links for the post-->
<div class="card mb-3">
  <div class="row g-0">
    <div class="col-md-4">
      {% if post.author.profile.profile_pic %}
      <img
        src=" {{ post.author.profile.profile_pic.url }}"
        width="200"
        height="200"
      />
      {% endif %}
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">
          {{ post.author.first_name}} - {{ post.author.last_name}}
        </h5>
        <p class="text-muted">
          {% if post.author.profile.website_url %}
          <a href="{{ post.author.profile.website_url }}"> Website </a>| 
          {% endif %} 
          {% if post.author.profile.facebook_url %}
          <a href="{{ post.author.profile.facebook_url }}"> Facebook </a>| 
          {% endif %} 
          {% if post.author.profile.twitter_url %}
          <a href="{{ post.author.profile.twitter_url }}"> Twitter </a>| 
          {% endif %} 
          
          {% if post.author.profile.instagram_url %}
          <a href="{{ post.author.profile.instagram_url }}"> Instagram </a>| 
          {% endif %}

        </p>
        <p class="card-text">{{ post.author.profile.bio }}</p>
      </div>
    </div>
  </div>
</div>
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)

## License
[MIT](https://choosealicense.com/licenses/mit/)
