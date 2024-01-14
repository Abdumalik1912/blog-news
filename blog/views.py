from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


class BlogPage(ListView):
    model = Post
    template_name = "home.html"


class BlogPostPage(DetailView):
    model = Post
    template_name = "detailed_post.html"


class CreateBlogPost(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "author", "body"]


class UpdateBlogPost(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ["title", "body"]


class DeleteBlogPost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")