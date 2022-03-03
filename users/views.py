from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import RegistrationForm, EditProfileForm
from .models import AdvUser


class LoginUserView(LoginView):
    template_name = 'users/login.html'


class LogoutUserView(LogoutView):
    pass


class RegistrationUserView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:posts')
    form_class = RegistrationForm


class EditProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_edit.html'
    form_class = EditProfileForm
    model = AdvUser
    success_url = reverse_lazy('blog:posts')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(EditProfileView, self).setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    template_name = 'users/'
