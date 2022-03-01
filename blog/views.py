from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.forms import CreateUpdatePost
from blog.models import Posts
from users.models import AdvUser


class ListPostsView(ListView):
    template_name = 'blog/posts.html'
    paginate_by = 4

    def get_queryset(self):
        return Posts.objects.filter(active=True, featured=True)


class DetailPostView(DetailView):
    template_name = 'blog/read_post.html'

    def get_object(self, queryset=None):
        return Posts.objects.select_related('author').get(slug=self.kwargs['slug'])

    # def get_context_data(self, **kwargs):
    #     context = super(DetailPostView, self).get_context_data(**kwargs)
    #     context['post_author'] = AdvUser.objects.get(username=self.object.author)
    #     return context


class ListPostUserView(LoginRequiredMixin, ListView):
    template_name = 'blog/posts_users.html'

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = CreateUpdatePost
    template_name = 'blog/create_update_post.html'
    success_url = reverse_lazy('blog:posts')

    def get_initial(self):
        return {
            'author': self.request.user,
            'active': True,
            'featured': True,
        }


class UpdatePostView(LoginRequiredMixin, UpdateView):
    form_class = CreateUpdatePost
    template_name = 'blog/create_update_post.html'
    success_url = reverse_lazy('blog:posts')

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:posts')
