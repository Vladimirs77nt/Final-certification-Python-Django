from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
   return render(request, 'recipe_app/index.html')

def recipe_all(request):
   return render(request, 'recipe_app/recipe_all.html')

def recipe(request):
   return HttpResponse("Страница - РЕЦЕПТ №... ")

def authorization(request):
    return HttpResponse("СТРАНИЦА АВТОРИЗАЦИИ")

def registrtion(request):
    return HttpResponse("СТРАНИЦА РЕГИСТРАЦИИ")