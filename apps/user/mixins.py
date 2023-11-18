from django.contrib.auth import views
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.user.models import User


class SupervisorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if (
            not request.user.is_authenticated
            or self.request.user.role != self.request.user.Role.SUPERVISOR
        ):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserRedirectMixin:
    """
    Use this in LoginView to redirect authenticate users
    """

    def get_success_url(self: views.LoginView):
        if url := self.get_redirect_url():
            return url
        user: User = self.request.user
        if user.role == User.Role.CLIENT:
            return reverse("website:home")
        if user.role == User.Role.SUPERVISOR:
            return reverse("dashboard:home")
        else:
            raise ImproperlyConfigured("User should be one of [CLIENT, SUPERVISOR]")
