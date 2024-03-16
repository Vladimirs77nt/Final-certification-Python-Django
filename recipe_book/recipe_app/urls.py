from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_all/', views.recipe_all, name='recipe_all'),
    path('author_all/', views.author_all, name='author_all'),

    path('recipe/<int:recipe_id>/', views.recipe_id, name='recipe_id'),
    path('authorization/', views.authorization, name='authorization'),
    path('registrtion/', views.registrtion, name='registrtion'),
]