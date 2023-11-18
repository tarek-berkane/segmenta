from django.views import generic


from apps.dashboard.mixins import DashboardMixin, HeaderMixin


class Home(DashboardMixin, generic.TemplateView):
    section_name = "home"
    template_name = "dashboard/main/home.html"


class DashboardSettingsSectionView(DashboardMixin, HeaderMixin, generic.TemplateView):
    header_name = "section"
    section_name = "settings"
    template_name = "dashboard/settings/section.html"
