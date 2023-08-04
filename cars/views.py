from django.shortcuts import render

from cars.models import FavoriCarsModel,BestCarsModel


def cars(request):
    favoriCar = FavoriCarsModel.objects.all()
    bestCar = BestCarsModel.objects.all()

    cars = {
        'favcar':favoriCar,
        'bestcar':bestCar
    }
    return render(request,'cars/index.html',cars)