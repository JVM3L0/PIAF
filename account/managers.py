from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, username, email, password, save=False, **extra_fields):
        if not username:
            raise ValueError("O nome de usuário é obrigatório")
        if not email:
            raise ValueError("O email é obrigatório")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)

        if save:
            user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            username, email, password, save=True, **extra_fields
        )
