from django.contrib import admin

from cars.models import FavoriCarsModel,BestCarsModel

# Register your models here.
@admin.register(FavoriCarsModel)
class AdminFavoriCars(admin.ModelAdmin):
    list_display = ('id','title','description')


@admin.register(BestCarsModel)
class AdminBestCars(admin.ModelAdmin):
    list_display = ('id','image','price')

