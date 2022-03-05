from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView
from django.forms import inlineformset_factory, HiddenInput
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render

from .forms import RegistrationForm, EditProfileForm
from .models import AdvUser, Social


class LoginUserView(LoginView):
    template_name = 'users/login.html'


class LogoutUserView(LogoutView):
    pass


class RegistrationUserView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:posts')
    form_class = RegistrationForm


@login_required
def edit_profile(request):
    SocialFormSet = inlineformset_factory(AdvUser, Social, fields=('name', 'link',))
    form = EditProfileForm(instance=request.user)
    formset = SocialFormSet(instance=request.user)
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        formset = SocialFormSet(request.POST, instance=request.user)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return HttpResponseRedirect(reverse('users:profile_edit'))
    context = {'form': form, 'formset': formset}
    return render(request, 'users/profile_edit.html', context)


# class EditProfileView(LoginRequiredMixin, UpdateView):
#     template_name = 'users/profile_edit.html'
#     form_class = EditProfileForm
#     model = AdvUser
#     success_url = reverse_lazy('blog:posts')
#
#     def setup(self, request, *args, **kwargs):
#         self.user_id = request.user.pk
#         return super(EditProfileView, self).setup(request, *args, **kwargs)
#
#     def get_object(self, queryset=None):
#         if not queryset:
#             queryset = self.get_queryset()
#         return get_object_or_404(queryset, pk=self.user_id)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    template_name = 'users/delete_profile.html'
    model = AdvUser
    success_url = reverse_lazy('blog:posts')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(DeleteUserView, self).setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return super(DeleteUserView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangePasswordUserView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:profile_edit')


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset/password_reset.html'
    subject_template_name = 'users/password_reset/reset_subject.txt'
    email_template_name = 'users/password_reset/reset_email.txt'
    success_url = reverse_lazy('users:password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if AdvUser.objects.filter(email=email).exists():
            return super(UserPasswordResetView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset/email_sent.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset/confirm_password.html'
    success_url = reverse_lazy('users:login')
