from django.shortcuts import render
from about.models import AboutModel
from blog.models import BlogModel

from cars.models import FavoriCarsModel,BestCarsModel

# Create your views here.
def home(request):
    bestcar = FavoriCarsModel.objects.all()
    about = AboutModel.objects.last()
    car = BestCarsModel.objects.all()
    blog = BlogModel.objects.all()
    val = {
        'car':bestcar,
        'about':about,
        'bestcar':car,
        'blog':blog
    }
    return render(request,'home/index.html',val)