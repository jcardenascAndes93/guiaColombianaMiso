from django.db import models

# Create your models here.

# Modelo City


class City(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


# Modelo Guia
class Guia(models.Model):
    full_name = models.CharField(max_length=50)
    frase = models.CharField(max_length=150)
    email = models.EmailField()
    photo = models.ImageField(upload_to='staticfiles/images', null=True)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


# Modelo Tourist
class Tourist(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email = models.EmailField()
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name + self.last_name


# Model Place
class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model Category
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Model Tour
class Tour(models.Model):

    name = models.CharField(max_length=50)
    map = models.ImageField(upload_to='staticfiles/images', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.name
