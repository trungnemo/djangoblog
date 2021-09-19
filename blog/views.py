from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
#Use the customized form
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy
# #Home 1
# def home(request):
#     return render(request, 'home.html', {})

#Home view version 2
# List all Posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['id']: id order 1,2,3...n
    # ordering = ['-id']: id order n,..3,2,1
    # ordering = ['-id']
    ordering = ['-post_date']

    # Add Category to navbar
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

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

# To Update a post
class BlogEditView(UpdateView):
    model = Post
    template_name = 'blogedit.html'
    #Rem the fields of we use the Custom form
    #fields = ['title', 'title_tag', 'body']
    form_class = PostEditForm

# To Delete a post
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogdelete.html'
    # After a post is deleted, it will be redrected to home page, 
    # Delete use this method, nos as BlogEditView with get_absolute_url in the models
    success_url = reverse_lazy('home')
# Category views
class CategoryAddView(CreateView):
    model = Category
    template_name = 'categoryadd.html'
    fields = '__all__'
#CategoryPostsView: List all posts by category
def CategoryPostsView(request, cats):
    #cats is the paramters passed in for filter all posts  of category
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categoryposts.html', {'cats':cats,'category_posts':category_posts})

