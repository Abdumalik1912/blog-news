from django.urls import path
from .views import BlogPage, BlogPostPage, CreateBlogPost, UpdateBlogPost, DeleteBlogPost


urlpatterns = [
    path("", BlogPage.as_view(), name="home"),
    path("post/<int:pk>", BlogPostPage.as_view(), name="post"),
    path("post/new", CreateBlogPost.as_view(), name="new_post"),
    path("post/<int:pk>/edit", UpdateBlogPost.as_view(), name="edit_post"),
    path("post/<int:pk>/delete", DeleteBlogPost.as_view(), name="delete_post"),
]
