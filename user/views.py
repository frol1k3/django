from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse

class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("account", args=[self.request.user.id,])

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "registration.html"

class AccountView(DetailView):
    model = User
    template_name = "account.html"
    context_object_name = "account"

class UserLogoutVeiw(LogoutView):
    pass