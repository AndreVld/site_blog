from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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
    template_name = 'users/delete_profile.html'
    model = AdvUser
    success_url = reverse_lazy('blog:posts')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(DeleteUserView, self).setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        # messages.success(request, 'Пользователь удален!')
        return super(DeleteUserView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangePasswordUserView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:profile_edit')
