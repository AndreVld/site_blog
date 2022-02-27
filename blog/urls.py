from django.urls import path
from blog.views import ListPosts, CreatePost, UpdatePost

app_name = 'blog'

urlpatterns = [
    path('', ListPosts.as_view(), name='posts'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<slug:slug>', UpdatePost.as_view(), name='update_post'),
]
