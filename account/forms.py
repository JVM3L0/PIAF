from django import forms
from django.core.exceptions import ValidationError

from account.models import Account


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=255,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": " "}), label="Senha"
    )

    class Meta:
        model = Account
        fields = ["email", "password"]

    def clean(self):
        return self.data


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    complete_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "})
    )
    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "})
    )
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "data-mask": "(00) 00000-0000", "placeholder": " "}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"type": "password", "class": "form-control", "placeholder": " "}),
        label="Senha",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"type": "password", "class": "form-control", "placeholder": " "}),
        label="Senha",
    )

    class Meta:
        model = Account
        fields = [
            "username",
            "email",
            "complete_name",
            "birth_date",
            "contact",
            "password",
            "confirm_password",
        ]
        labels = {
            "username": "Nome",
            "email": "E-mail",
        }
        error_messages = {
            "username": {
                "required": 'O campo "Nome" é obrigatório.',
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if confirm_password != password:
            raise ValidationError('As senhas não coincidem.')

        return cleaned_data
