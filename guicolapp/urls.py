from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^guias', views.guias, name='addImage'),
]