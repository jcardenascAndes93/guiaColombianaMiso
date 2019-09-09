from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.http import HttpResponse
from psycopg2._psycopg import cursor

from guicolapp.models import Guia, City, Category
from .models import Tour

from rest_framework.response import Response
from rest_framework.views import APIView


@csrf_exempt
def guias(request):
    guias = Guia.objects.all()
    return HttpResponse(serializers.serialize("json", guias))


@csrf_exempt
def detalleGuias(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        guia = Guia.objects.filter(full_name=name)
        print(name)
    return render(request, "guicolapp/detalleGuias.html", {'name': name})


@csrf_exempt
def index(request):
    tour_list = Tour.objects.all()
    context = {'tours_list': tour_list}
    return render(request, 'guicolapp/index.html', context)


class TourView(APIView):
    def get(self, request, pk):
        tours = Tour.objects.filter(guia__pk=pk)
        return HttpResponse(serializers.serialize('json', tours))


class GuidesByCity(APIView):
    def get(self, request, idCity):
        guias = Guia.objects.filter(city=idCity)
        return HttpResponse(serializers.serialize('json', guias))


class getCities(APIView):
    def get(self, request):
        cities = City.objects.all()
        return HttpResponse(serializers.serialize('json', cities))


class getCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return HttpResponse(serializers.serialize('json', categories))


class guidesByCategory(APIView):
    def get(self, request, idCategory):
        guias = Guia.objects.raw(
            'select guicolapp_guia.id,guicolapp_guia.full_name from guicolapp_guia, guicolapp_tour, guicolapp_tour_categories, guicolapp_category where guicolapp_guia.id = guicolapp_tour.guia_id and guicolapp_tour.id = guicolapp_tour_categories.tour_id and guicolapp_tour_categories.category_id= guicolapp_category.id and guicolapp_category.id = ' + idCategory + '')
        return HttpResponse(serializers.serialize('json', guias))


class guidesByCategoryandCity(APIView):
    def get(self, request, idCategory, idCity):
        guias = Guia.objects.raw(
            'select guicolapp_guia.id,guicolapp_guia.full_name from guicolapp_city,guicolapp_guia, guicolapp_tour, guicolapp_tour_categories, guicolapp_category where guicolapp_guia.id = guicolapp_tour.guia_id and guicolapp_tour.id = guicolapp_tour_categories.tour_id and guicolapp_tour_categories.category_id= guicolapp_category.id and guicolapp_guia.city_id = guicolapp_city.id and guicolapp_category.id  = ' + idCategory + ' and guicolapp_city.id = ' + idCity + '')
        return HttpResponse(serializers.serialize('json', guias))
