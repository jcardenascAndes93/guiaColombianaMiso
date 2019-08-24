from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from guicolapp.models import Guia


def guias(request):
    guias = Guia.objects.all()
    paginator = Paginator(guias, 8)
    page = request.GET.get('page')

    guias = paginator.get_page(page)  # < New in 2.0!

    return render(request, 'guicolapp/guias.html', { 'guias': guias })