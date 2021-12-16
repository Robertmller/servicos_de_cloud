from django.contrib import admin
from django.urls import path, include

#from django.conf.urls import handler404, handler500

from core.views import error404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#handler404 = views.error404
#handler500 = views.error500
