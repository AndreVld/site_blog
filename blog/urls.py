from django.urls import path
from blog.views import ListPostsView, CreatePostView, UpdatePostView, DeletePostView

app_name = 'blog'

urlpatterns = [
    path('', ListPostsView.as_view(), name='posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('update_post/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<slug:slug>', DeletePostView.as_view(), name='delete_post'),
]
