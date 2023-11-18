from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy


from apps.dashboard.mixins import DashboardMixin
from apps.user.models import Supervisor, Client
from apps.user import forms as user_form


class DashboardLoginView(LoginView):
    template_name = "dashboard/auth/login.html"
    form_class = user_form.SupervisorAuthenticationForm
    next_page = "dashboard:home"


class DashboardLogoutView(LogoutView):
    next_page = "website:login"


class DashboardUserListView(DashboardMixin, generic.ListView):
    section_name = "user"
    template_name = "dashboard/user/list.html"
    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        return Supervisor.objects.all()


class DashboardUserCreateView(DashboardMixin, generic.CreateView):
    section_name = "user"
    form_class = user_form.SupervisorCreateForm
    template_name = "dashboard/user/form.html"

    def get_success_url(self) -> str:
        return reverse("dashboard:user-list")


class DashboardUserUpdateView(DashboardMixin, generic.UpdateView):
    section_name = "user"
    form_class = user_form.SupervisorCreateForm
    template_name = "dashboard/user/form.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Supervisor.objects.all()

    def get_success_url(self) -> str:
        return reverse("dashboard:user-list")


# ================================================================
# WEBSITE
# ================================================================


class WebsiteLoginView(LoginView):
    template_name = "website/auth/login.html"
    form_class = user_form.ClientAuthenticationForm
    next_page = "website:home"


class WebsiteSignupView(generic.FormView):
    template_name = "website/auth/signup.html"
    next_page = "website:login"
    form_class = user_form.ClientCreateForm
    success_url = reverse_lazy("website:home")

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class WebsitePasswordForgotView(generic.TemplateView):
    template_name = "website/auth/password_forgot.html"
