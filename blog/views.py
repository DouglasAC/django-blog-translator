from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'
    
class HomeView(generic.TemplateView):
    template_name = 'index.html'