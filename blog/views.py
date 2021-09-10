from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# #Home 1
# def home(request):
#     return render(request, 'home.html', {})
#Home view version 2
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
class BlogDetail(DetailView):
    model = Post
    template_name = 'blogdetail.html'
