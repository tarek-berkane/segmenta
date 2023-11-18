from django.urls import path

from apps.website import views as website_views
from apps.user import views as user_views

app_name = "website"

urlpatterns = [
    path("", website_views.HomeView.as_view(), name="home"),
    path(
        "products/paperless/", website_views.PaperLessView.as_view(), name="paperless"
    ),
    path(
        "products/business-insight/",
        website_views.BusinessInsightView.as_view(),
        name="business-insight",
    ),
    path(
        "products/customer-segmentation/",
        website_views.CustomerSegmentation.as_view(),
        name="customer-segmentation",
    ),
    path(
        "products/sales-forecast/",
        website_views.SalesForecast.as_view(),
        name="sales-forecast",
    ),
    # path(
    #     "products/business-insight/",
    #     website_views.BusinessInsightView.as_view(),
    #     name="business-insight",
    # ),
    # ===========================
    # Pricing
    # ===========================
    path("pricing/", website_views.PricingView.as_view(), name="pricing"),
    # ===========================
    # Invoice
    # ===========================
    path("invoice/", website_views.InvoiceView.as_view(), name="invoice"),
    # ===========================
    # auth
    # ===========================
    path("login/", user_views.WebsiteLoginView.as_view(), name="login"),
    path("signup/", user_views.WebsiteSignupView.as_view(), name="signup"),
    path(
        "password-forgot/",
        user_views.WebsitePasswordForgotView.as_view(),
        name="password-forgot",
    ),
    # ===========================
    # Term Policy
    # ===========================
    path("term-policy/", website_views.TermPolicyView.as_view(), name="term-policy"),
]
