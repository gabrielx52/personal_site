
"""Portfolio site views."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view class based view."""

    template_name = 'portfolio/home.html'
