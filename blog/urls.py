from django.urls import path

from blog import views


urlpatterns = [
    path('',views.blog),
    path('details/<int:detail_id>',views.details,name="details")
]
