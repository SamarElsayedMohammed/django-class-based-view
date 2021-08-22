from django.shortcuts import render
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView 
from . models import Post
# Create your views here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate():
    pass

class PostUpdate():
    pass

class PostDelete():
    pass



