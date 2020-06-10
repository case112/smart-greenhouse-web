from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from data.views import index #, temp_today, hum_today



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #path('temp-today/', temp_today, name='temp-today'),
    #path('hum-today/', hum_today, name='hum-today'),
]

