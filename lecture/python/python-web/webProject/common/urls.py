from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="common/login.html")),

]