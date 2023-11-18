from django.urls import path

from apps.dashboard import views as dashboard_views
from apps.user import views as user_views

app_name = "dashboard"

urlpatterns = [
    path("", dashboard_views.Home.as_view(), name="home"),
    # ============================
    # USER
    # ============================
    path("users/", user_views.DashboardUserListView.as_view(), name="user-list"),
    path(
        "users/create/",
        user_views.DashboardUserCreateView.as_view(),
        name="user-create",
    ),
    path(
        "users/<int:pk>/update/",
        user_views.DashboardUserUpdateView.as_view(),
        name="user-update",
    ),
    # ============================
    # Settings
    # ============================
    path(
        "settings/",
        dashboard_views.DashboardSettingsSectionView.as_view(),
        name="settings",
    ),
    # ============================
    # AUTH
    # ============================
    path("login/", user_views.DashboardLoginView.as_view(), name="login"),
    path("logout/", user_views.DashboardLogoutView.as_view(), name="logout"),
]
