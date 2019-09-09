from django.urls import path
from django.conf.urls import url
from .views import TourView, getCities, GuidesByCity, guidesByCategory, getCategories, guidesByCategoryandCity, \
    getTourPlaces, getCategoriesbyGuia
from . import views

urlpatterns = [

    url(r'^guias', views.guias, name='verGuias'),
    url(r'^detalleGuias', views.detalleGuias, name='detalleGuias'),
    path('tours/<int:pk>', TourView.as_view()),
    path('cityfilter/<int:idCity>', GuidesByCity.as_view()),
    path('getcities', getCities.as_view()),
    path('getcategories', getCategories.as_view()),
    path('categoryfilter/<str:idCategory>', guidesByCategory.as_view()),
    path('categorycityfilter/<str:idCategory>/<str:idCity>', guidesByCategoryandCity.as_view()),
    path('tourplaces/<str:idTour>', getTourPlaces.as_view()),
    path('categoriesbyguide/<str:idGuia>', getCategoriesbyGuia.as_view()),
]
