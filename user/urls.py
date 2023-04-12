from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from user import views


app_name = "user"

urlpatterns = [
    path('user/', views.UserView.as_view(), name="profile_url"),
    path('user/deactivation/', views.DeactivationUserView.as_view(), name="deactivation_url"),
    path('user/edit-data/', views.EditUserDataView.as_view(), name="edit_data_url"),
    path('user/edit-password/', views.EditUserPasswordView.as_view(), name="edit_password_url"),
    path(settings.LOGIN_URL[1:], views.SignInView.as_view(), name="signin_url"),
    path('sign-up/', views.SignUpView.as_view(), name="signup_url"),
    path('logout/', LogoutView.as_view(next_page='catalog:home_url'), name='logout_url'),
]