from django.urls import path
from blog.views import ListPostsView, CreatePostView, UpdatePostView, DeletePostView, ListPostUserView, DetailPostView

app_name = 'blog'

urlpatterns = [
    path('', ListPostsView.as_view(), name='posts'),
    path('read_post/<slug:slug>', DetailPostView.as_view(), name='read_post'),
    path('my_posts/', ListPostUserView.as_view(), name='posts_user'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('update_post/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<slug:slug>', DeletePostView.as_view(), name='delete_post'),


]
