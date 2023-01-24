from accounts.views import user_login, user_logout, signup
from django.urls import path


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout")
]
