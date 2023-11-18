from django import template
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag
def update_param(request, param):
    # Get the current GET parameters from the request
    params = dict(request.GET.copy())
    # Update the 'page' parameter with the provided value
    params["page"] = param
    # Return the updated URL
    return f"{request.path}?{urlencode(params,doseq=True)}"
