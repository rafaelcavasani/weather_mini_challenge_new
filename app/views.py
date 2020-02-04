from django.views.generic import TemplateView
from .service import get_weather
from datetime import datetime

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        now = datetime.now()
        formatted_now = now.strftime('%Y-%m-%d')
        context = super().get_context_data(**kwargs)
        context['now'] = formatted_now
        return context

class WeatherView(TemplateView):
    template_name = "weather.html"

    def get_context_data(self, **kwargs):
        get_weather()
        context = super().get_context_data(**kwargs)
        context['ret'] = ret
        return context


