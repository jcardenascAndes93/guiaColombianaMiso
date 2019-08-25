from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^guias', views.guias, name='verGuias'),
    url(r'^detalleGuias', views.detalleGuias, name='detalleGuias')
]