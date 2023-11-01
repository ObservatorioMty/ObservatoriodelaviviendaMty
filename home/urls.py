from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', HomeView.as_view(template_name="home.html")),
    path('', HomeView.as_view(), name='home'),
    path('terminos', TerminosView.as_view(), name='terminos'),

]