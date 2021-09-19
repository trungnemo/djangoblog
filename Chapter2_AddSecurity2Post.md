# Apply the simple security for Authorized users

## Simple security 1: Only owner can edit, delete his own posts
- {% if user.is_authenticated %} to let users goto the add page
- {% user.id == post.author.id %} to check if user can see his or her own post for edting
```html
<!--in the home page or detail page, check to enable the edit, delete links-->
{% if user.is_authenticated and user.id == post.author.id %}
    <small><a href="{% url 'blogedit' post.pk %}">(Edit)</a></small> -
    <small><a href="{% url 'blogdelete' post.pk %}">(Delete)</a></small>
{% endif %}
```
- if users go directly to the page by input the url in the browser address, we add this to to the page
```html
<!--in the edit page-->
{% extends 'base.html' %}
<!--Title-->
{% block title%}
<title>Blog Edit Page</title>
{% endblock %}
<!-- Content-->
{% block content%}
<div class="container">
  {% if user.is_authenticated and user.id == post.author.id %}
  <h3 class="mt-5 text-center">Edit a post</h3>
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-secondary">Submit</button>
  </form>
  {% else %}
  <p>Page not found 404</p>
  {% endif %}
</div>
{% endblock %}
```

## Simple security 2: Set the author by the current logon used for new posts
Cause the browsers from users's devices do not know the logon user to auto set the author for the post. Only the servers know. 
We do it by
- Replace the author field in the edit form, from the Select to TextField with type hidden.
- At the html page, we use the java script to update the text value with the author id
```python

#Customized form for the Post model
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category','body')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authorid', 'type':'hidden'}),
            # 'category': forms.Select(choices = choices, attrs={'class':'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'})
        }
```
We use the jave script to find the authorid html tag and replace the value with the user id
```html
{% extends 'base.html' %}
<!--Title page-->
{% block title%}
<title>Post Add</title>
{% endblock%}

<!--Title page-->
{% block content%}
<h1 class="mt-5 text-center">Add a new Post</h1>
<!-- Version of Django Form no Bootstrap

<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button class="btn btn-primary">Submit</button>
</form>

end of first version -->

{% if user.is_authenticated %}
<!--Customized form with bootstrap-->
<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-primary">Submit</button>
  </form>
</div>

<script>
  var authorvalue = "{{ user.id }}";
  document.getElementById("authorid").value = authorvalue;
</script>

{% else %}
<p>You are not authiticated to go on more...!</p>
{% endif %} {% endblock%}

```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
I use this to teach my son
## License
[MIT](https://choosealicense.com/licenses/mit/)
