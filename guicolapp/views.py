from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Tour
# Create your views here.


def index(request):
    tour_list = Tour.objects.all()
    context = {'tours_list': tour_list}
    return render(request, 'guicolapp/list_tours.html', context)
