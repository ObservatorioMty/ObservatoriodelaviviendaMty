"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found

def custom_page_not_found(request, exception):
    return page_not_found(request, exception, template_name='404.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('zona.urls')),
    path('', include('inmueble.urls')),
    path('', include('investigacion.urls')),
    path('', include('equipo.urls')),
   
]
from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
