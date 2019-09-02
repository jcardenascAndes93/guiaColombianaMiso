from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.http import HttpResponse
from guicolapp.models import Guia
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
