from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from apps.user.models import User


class RoleRequired(UserPassesTestMixin):
    def get_required_role(self):
        raise NotImplementedError(
            "{} is missing the implementation of the get_required_role() method.".format(
                self.__class__.__name__
            )
        )

    def test_func(self) -> bool | None:
        request: HttpRequest = self.request
        user: User = request.user
        if request.user.is_authenticated:
            if user.role == self.get_required_role():
                return True
        return False

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect("login")


class ClientOrAnonymousRoleRequired(RoleRequired):
    def test_func(self) -> bool | None:
        request: HttpRequest = self.request
        user: User = request.user
        if user.is_anonymous:
            return True
        if user.role == user.Role.CLIENT:
            return True
        return False

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse(settings.WEBSITE_LOGIN_URL))


class ClientRoleRequired(RoleRequired):
    def get_required_role(self):
        return User.Role.CLIENT

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse(settings.WEBSITE_LOGIN_URL))


class SupervisorRoleRequired(RoleRequired):
    def get_required_role(self):
        return User.Role.SUPERVISOR

    def handle_no_permission(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(reverse(settings.DASHBOARD_LOGIN_URL))
