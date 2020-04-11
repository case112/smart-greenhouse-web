from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from data.views import index, temperature_chart



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('temperature-chart/', temperature_chart, name='temperature-chart'),
]

