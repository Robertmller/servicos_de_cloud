from django.contrib import admin
from django.urls import path, include
#from django.core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
