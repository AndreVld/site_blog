from django.urls import path

from .views import LoginUserView, LogoutUserView, RegistrationUserView, EditProfileView, DeleteUserView, \
    ChangePasswordUserView, UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView

app_name = 'users'

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),

    path('registration', RegistrationUserView.as_view(), name='register'),
    path('profile_edit', EditProfileView.as_view(), name='profile_edit'),
    path('delete_profile', DeleteUserView.as_view(), name='delete_profile'),

    path('change_password', ChangePasswordUserView.as_view(), name='change_password'),

    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/reset/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

]
