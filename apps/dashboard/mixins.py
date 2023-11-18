from django.core.exceptions import ImproperlyConfigured
from apps.user.mixins import SupervisorRequiredMixin


class MenuMixin:
    SECTION_NAME = "section_name"
    SUB_SECTION_NAME = "subsection_name"

    section_name: str = None
    subsection_name: str = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_submenu_data())
        return context

    def get_submenu_data(self):
        context = {}
        if self.section_name:
            context[self.SECTION_NAME] = self.section_name
            context[self.SUB_SECTION_NAME] = self.subsection_name  # null allowed
            return context

        raise ImproperlyConfigured(
            f"{self.__class__.__name__} should implement section_name attribute extended from MenuMixin"
        )


class HeaderMixin:
    HEADER_NAME = "header_name"
    header_name: str = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_header_product_data())
        return context

    def get_header_product_data(self):
        context = {}
        if self.header_name:
            context[self.HEADER_NAME] = self.header_name
            return context

        raise ImproperlyConfigured(
            f"{self.__class__.__name__} should implement {self.HEADER_NAME} {HeaderMixin.__name__}"
        )


class DashboardMixin(SupervisorRequiredMixin, MenuMixin):
    login_url = "dashboard:login"
