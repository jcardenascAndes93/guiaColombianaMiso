from django.urls import path
from django.conf.urls import url
from .views import TourView, getCities, GuidesByCity, guidesByCategory, getCategories
from . import views

urlpatterns = [

    url(r'^guias', views.guias, name='verGuias'),
    url(r'^detalleGuias', views.detalleGuias, name='detalleGuias'),
    path('tours/<int:pk>', TourView.as_view()),
    path('cityfilter/<int:idCity>', GuidesByCity.as_view()),
    path('getcities', getCities.as_view()),
    path('getcategories', getCategories.as_view()),
    path('categoryfilter/<str:idCategory>', guidesByCategory.as_view()),
]
