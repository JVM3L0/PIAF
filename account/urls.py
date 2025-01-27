from django.urls import path
from .views import RegisterView, LoginView, HomeView, LogoutView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("", HomeView.as_view(), name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
