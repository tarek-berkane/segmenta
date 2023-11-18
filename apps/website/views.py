from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "website/home/home.html"


class PaperLessView(generic.TemplateView):
    template_name = "website/products/paperless/index.html"


class BusinessInsightView(generic.TemplateView):
    template_name = "website/products/business_insights/index.html"


class CustomerSegmentation(generic.TemplateView):
    template_name = "website/products/customer_segmentation/index.html"


class SalesForecast(generic.TemplateView):
    template_name = "website/products/sales_forecast/index.html"


class PricingView(generic.TemplateView):
    template_name = "website/pricing/index.html"


class InvoiceView(generic.TemplateView):
    template_name = "website/invoice/index.html"


class TermPolicyView(generic.TemplateView):
    template_name = "website/term_policy.html"
