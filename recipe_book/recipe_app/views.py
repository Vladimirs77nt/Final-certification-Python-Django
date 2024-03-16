import datetime
import logging
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from .forms import AuthorForm, CommentForm, RecipeForm, CategoryForm
from .models import Author, Comment2, Recipe, Category

# главная страница
def index(request):
   return render(request, 'recipe_app/index.html')

# Все рецепты
def recipe_all(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_app/recipe_all.html', {'recipes': recipes})

# Все авторы
def author_all(request):
    authors = Author.objects.all()
    return render(request, 'recipe_app/author_all.html', {'authors': authors})

# Все рецепты автора
def author_recipes(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'recipe_app/author_recipes.html', {'author': author, 'recipes': recipes})

# страница рецепта по id
def recipe_id(request, recipe_id):
    recipe_get = get_object_or_404(Recipe, pk=recipe_id)
    author = recipe_get.author
    comments = Comment2.objects.filter(recipe=recipe_get).order_by('-date_create')
    recipe = {'title':recipe_get.title,
              'description': recipe_get.description,
              'ingredients':recipe_get.ingredients}
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            comment = Comment2(author = author,
                              content = content,
                              recipe = recipe_get
                              )
            comment.save()
            return redirect('recipe_full', recipe_id)
    else:
        form = CommentForm()

    recipe_get.save()
    return render(request, 'recipe_app/recipe_full.html', {'recipe': recipe_get, 'author': author, 'comments': comments, 'form':form})


# Добавление нового автора
def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'Автор сохранен'
            return redirect('author_form')
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'recipe_app/author_form.html', {'form':form, 'message':message})

def recipe(request):
   return HttpResponse("Страница - РЕЦЕПТ №... ")

def authorization(request):
    return HttpResponse("СТРАНИЦА АВТОРИЗАЦИИ")

def registrtion(request):
    return HttpResponse("СТРАНИЦА РЕГИСТРАЦИИ")