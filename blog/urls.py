from django.urls import path
from django.views.generic import TemplateView

from site_blog import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/posts.html'), name='posts'),
]
