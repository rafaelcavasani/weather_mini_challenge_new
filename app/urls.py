from django.urls import path, include
from .views import IndexView, WeatherView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('weather/', WeatherView.as_view(), name='weather')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
