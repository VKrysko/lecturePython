from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),

    path("add", views.add, name="add"),
    path("<title>", views.entri ),
    path("<title>/edit", views.edit, name="edit"),
    path("search/", views.search, name='search'),
    path("random_page/", views.random_page, name='random_page')
   
]
