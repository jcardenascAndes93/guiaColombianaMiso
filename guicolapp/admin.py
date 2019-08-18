from django.contrib import admin

from .models import City
from .models import Tour
from .models import Category
from .models import Place
from .models import Guia
from .models import Tourist

# Register your models here.

admin.site.register(City)
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Guia)
admin.site.register(Tourist)

