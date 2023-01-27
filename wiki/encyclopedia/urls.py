from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("newPage", views.addNewPage, name="addNewPage"),
    path("page", views.getPage, name="getPage"),
    path("random", views.getRandomPage, name="getRandomPage")
]
