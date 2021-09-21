from django.contrib.auth.forms import UserChangeForm, UserCreationForm , UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User 
from django import forms
from django.forms.widgets import EmailInput 

#Custome form for registragion
class SignUpForm(UserCreationForm):
    #email = forms.EmailField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    #first_name = forms.CharField(max_length = 100)
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    #last_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Overwrite the attribute of username, password
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

#Edit Profile Form
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User name'}))
    last_login = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last login'}))
    is_supperuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField( widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField( widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password','last_login', 'is_supperuser','is_staff','is_active','date_joined')


#Custome form for registragion
class BlogPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2= forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')