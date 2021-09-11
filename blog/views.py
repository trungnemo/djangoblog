from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
#Use the customized form
from .forms import PostForm
# #Home 1
# def home(request):
#     return render(request, 'home.html', {})

#Home view version 2
# List all Posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
# Detail Post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogdetail.html'
# # Post Add to add a new post
# class BlogAddView(CreateView):
#     model = Post
#     template_name = 'blogadd.html'
#     # Soame specified fields in the form only
#     # fields = ('title','title_tag', 'body','author')
#     # All fields will appear in the form
#     fields = '__all__'

# Modify the BlogAddView to use the custom form: PostForm
class BlogAddView(CreateView):
    model = Post
    #Just Add this to use the custom form
    #and remove the fields = (cause the PostForm take care all of the fields)
    form_class = PostForm 
    template_name = 'blogadd.html'
    