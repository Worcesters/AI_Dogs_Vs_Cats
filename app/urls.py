from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
	path('load_image', api.load_image),
    path('errorReport', api.errorReport),
]
