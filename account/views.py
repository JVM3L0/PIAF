from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, RegisterForm
from .models import Account


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "auth/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            complete_name = form.cleaned_data.get("complete_name")
            birth_date = form.cleaned_data.get("birth_date")
            contact = form.cleaned_data.get("contact")
            password = form.cleaned_data.get("password")

            account = Account.objects.create_user(
                username=username,
                email=email,
                password=password,
                complete_name=complete_name,
                birth_date=birth_date,
                contact=contact,
                save=True,
            )

            return redirect("login")

        for error in form.non_field_errors():
            messages.error(request, error)
        for field, errors in form.errors.items():
            for error in errors:
                if field == "__all__":
                    continue
                messages.error(request, f"{field.upper()}: {error}")

        return render(request, "auth/signup.html", {"form": form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            if not Account.objects.filter(email=email).exists():
                messages.error(request, "Conta não cadastrada.")
                return redirect("home")

            account = authenticate(request, email=email, password=password)

            if account:
                login(request, account)
                return redirect("home")
            else:
                messages.error(request, "Informações inválidas.")

        for error in form.non_field_errors():
            messages.error(request, error)
        for field, errors in form.errors.items():
            for error in errors:
                if field == "__all__":
                    continue
                messages.error(request, f"{field.upper()}: {error}")

        return redirect("login")


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        account = request.user
        return render(request, "content/home.html", {"account": account})
