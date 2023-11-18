from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        SUPERVISOR = "SUPERVISOR", "Supervisor"

    base_role = Role.CLIENT

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role

        return super().save(*args, **kwargs)


class ClientManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Client(User):
    base_role = User.Role.CLIENT

    objects = ClientManager()

    class Meta:
        proxy = True


class SupervisorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SUPERVISOR)


class Supervisor(User):
    base_role = User.Role.SUPERVISOR

    objects = SupervisorManager()

    class Meta:
        proxy = True
