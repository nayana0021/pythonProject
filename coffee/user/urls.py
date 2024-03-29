from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views


app_name = "user"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("user:login"),
        ),
        name="password_change",
    ),
]
