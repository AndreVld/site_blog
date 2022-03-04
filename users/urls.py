from django.urls import path

from .views import LoginUserView, LogoutUserView, RegistrationUserView, EditProfileView, DeleteUserView

app_name = 'users'

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('registration', RegistrationUserView.as_view(), name='register'),
    path('profile_edit', EditProfileView.as_view(), name='profile_edit'),
    path('delete_profile', DeleteUserView.as_view(), name='delete_profile'),


]
