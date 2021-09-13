# Sum up Chapter 1 to 6
Now that time for a break with sum-up before go next
## The steps to add a new page/new function
```python
#step 1
def step1_define_model():
    #add a class model in models.py
    #run command : python manage.py makemigrations
    #run command : python manage.py migrate
def step2_define_customform():
    #add a forms.py
    from django import forms
    from .models import Post 
    #Customized form for the Post model
    class PostForm(forms.ModelForm):
        model = Post 
        fields = ('title', 'title_tag', 'author', 'body')
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
        }
def step3_define_view():
   #if use a def then use the return render(request, 'template.html', {})
   #if use the class view for example 
   class BlogAddView(CreateView):
         model = Post
         template_name =   
         form_class = PostForm
         success_url = reverse_lazy('home') 
def step4_define_urls():
    from .views import HomeView, BlogDetailView, BlogAddView, BlogEditView, BlogDeleteView
    urlpatterns = [
         path('blogadd/', BlogAddView.as_view(), name = "blogadd"),
    ]

```
## Django authentication
Check if the user is login successfully/is authenticated
```python
{% user.is_authenticated %}
```
Check if the logon user can edit his own data by enable the edit, delete links
```html
{% if user.is_authenticated and user.id == post.author.id %}
    <small><a href="{% url 'blogedit' post.pk %}">(Edit)</a></small> -
    <small><a href="{% url 'blogdelete' post.pk %}">(Delete)</a></small>
{% endif %}
```
Formating the post content
- django by default remove all the html tags in the text content
- so we might use
```html
    <!-- just show first 200 chars of Body -->
    <!-- We add |safe to tell django does not remove the html tag in the body text of the blog-->
    {{ post.body | slice:":200" |safe}}
```

## Contributing
By [TrungVan](https://www.facebook.com/trungnemo)
## License
[MIT](https://choosealicense.com/licenses/mit/)

