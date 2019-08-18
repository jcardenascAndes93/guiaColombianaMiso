from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Tour

def index(request):
    tour_list = Tour.objects.all()
    context = {'tours_list' : tour_list}
    return render(request, 'guicolapp/list_tours.html', context)