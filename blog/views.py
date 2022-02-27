from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from blog.forms import CreateUpdatePost
from blog.models import Posts


class ListPosts(ListView):
    model = Posts
    template_name = 'blog/posts.html'

    def get_queryset(self):
        return Posts.objects.filter(active=True, featured=True)


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreateUpdatePost
    template_name = 'blog/create_update_post.html'
    success_url = reverse_lazy('blog:posts')

    def get_initial(self):
        return {
            'author': self.request.user,
            'active': True,
            'featured': True,
        }


class UpdatePost(LoginRequiredMixin, UpdateView):
    form_class = CreateUpdatePost
    template_name = 'blog/create_update_post.html'
    success_url = reverse_lazy('blog:posts')

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])