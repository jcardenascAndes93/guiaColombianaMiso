from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# Create your views here.

from .forms import SignUpForm

from .models import Tour
from .models import Tourist


def index(request):
    tour_list = Tour.objects.all()
    context = {'tours_list' : tour_list}
    return render(request, 'guicolapp/list_tours.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'useraccounts/signup.html', {'form': form})
