from django import forms
from .models import Post , Category

#Temp data to simulate the category select form control
#We define the data type list of turple

#choices = [('Sport','Sport'), ('Music','Music'), ('Reading','Reading')]

choices = Category.objects.all().values_list('name','name')
choice_list = []
for c in choices:
    choice_list.append(c)

#Customized form for the Post model
class PostForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'category','body', 'snippet')
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
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'}),
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Post snippet'})
        }

class PostEditForm(forms.ModelForm):
    # Class to holde the infor for the Form: Model, Model Fields
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'category', 'body','snippet')
        # dictionary to specify the kind of html input types for each fields
        widgets = {
            #from.[TextInput, Select, Textarea are the form input types]
            # attrs={'class':'form-control'}: is the html class style sheet from bootstrap
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
            'category': forms.Select(choices = choices, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Body for long text'}),
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Post snippet'})
        }