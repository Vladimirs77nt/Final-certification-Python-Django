from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_all/', views.recipe_all, name='recipe_all'),
    path('recipe/', views.recipe, name='recipe'),
    path('authorization/', views.authorization, name='authorization'),
    path('registrtion/', views.registrtion, name='registrtion'),
]