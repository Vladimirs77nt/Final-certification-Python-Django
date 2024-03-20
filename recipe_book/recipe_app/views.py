import logging
import random
from django import forms
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .forms import AuthorForm, RecipeForm, UserRegisterForm, UserLoginForm
from .models import Author, Recipe, Category

logger = logging.getLogger(__name__)


#----------------------------------------------
# случайный список (set) из <count> рецептов
def random_recipes (count):
    recipes = Recipe.objects.all()
    recipes_random = set()
    recipes_count = recipes.count()
    if count > recipes_count:
        i = recipes_count
    else:
        i = count
    while len(recipes_random) < i:
        recipe_random = random.choice(recipes)
        recipes_random.add(recipe_random)
    return recipes_random

# случайный список (set) из <count> авторов
def random_authors (count):
    authors = Author.objects.all()
    authors_random = set()
    authors_count = authors.count()
    if count > authors_count:
        i = authors_count
    else:
        i = count
    while len(authors_random) < i:
        recipe_random = random.choice(authors)
        authors_random.add(recipe_random)
    return authors_random

#----------------------------------------------
# главная страница
def index(request):
   authors = random_authors(3)
   recipes = random_recipes(3)
   return render(request, 'recipe_app/index.html',
                 {'recipes': recipes, 'authors':authors})

# Все рецепты
def recipe_all(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_app/recipe_all.html', {'recipes': recipes})

# Все авторы
def author_all(request):
    authors = Author.objects.all()
    return render(request, 'recipe_app/author_all.html', {'authors': authors})

#----------------------------------------------
# страница отображения рецепта по id
def recipe_id(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = recipe.author
    return render(request, 'recipe_app/recipe_id_view.html', {'recipe': recipe, 'author':author})

#----------------------------------------------
# страница редактирования рецепта по id
def recipe_id_edit(request, recipe_id):
    recipe_get = get_object_or_404(Recipe, pk=recipe_id)
    image_old = recipe_get.photo
    author = recipe_get.author
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            steps_cooking = form.cleaned_data['steps_cooking']
            aboutime_for_cookingt = form.cleaned_data['aboutime_for_cookingt']
            photo = form.cleaned_data['photo']
            author = form.cleaned_data['author']

            if photo:
                print (f"изображение: загружено новое изображение {photo}")
                recipe = Recipe(pk = recipe_id,
                                title=title,
                                description=description,
                                ingredients=ingredients,
                                steps_cooking=steps_cooking,
                                aboutime_for_cookingt=aboutime_for_cookingt,
                                photo=photo,
                                author = author,
                                )
                fs = FileSystemStorage()    # загруженное изображение
                print ('fs =', fs)
                fs.save(photo.name, photo)  # сохранение в папку 'media'
            else:
                print ("изображение: НОВОЕ ИЗОБРАЖЕНИЕ НЕ ЗАГРУЖЕНО !")
                recipe = Recipe(pk = recipe_id,
                                title=title,
                                description=description,
                                ingredients=ingredients,
                                steps_cooking=steps_cooking,
                                aboutime_for_cookingt=aboutime_for_cookingt,
                                photo=image_old,
                                author = author,
                                )
            recipe.save()
            return redirect('recipe_id', recipe_id)
        else:
            print ('валидация НЕ пройдена !!!')
    else:
        form = RecipeForm(instance=recipe_get)

    return render(request, 'recipe_app/recipe_id.html', {'recipe': recipe_get, 'form':form})

#----------------------------------------------
# страница автора по id
def author_id(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'recipe_app/author_id.html', {'author': author, 'recipes': recipes})

#----------------------------------------------
# Форма добавления нового автора
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


#----------------------------------------------
# Форма РЕГИСТРАЦИИ автора
def registration(request):
  print ("запущена форма регистрации")
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      print ("получены данные <form> регистрации")
      username = form.cleaned_data.get('username')
      author = Author(username=username,
                      name=username,
                      birthday='1900-01-01',
                      set_password=form.cleaned_data.get('password1'),
                      email=form.cleaned_data.get('email'),
                      )
      author.save()
      print(request, f"Аккаунт <{username}> - создан!")
      messages.success(request, f"Аккаунт <{username}> - создан!")
      return redirect('index')
  else:
    form = UserRegisterForm()
  return render(request, 'recipe_app/registration.html', {'form': form})

#----------------------------------------------
# Форма АВТОРИЗАЦИИ автора
def authorization(request):
  print ("запущена форма авторизации")
  if request.method == "POST":
    form = UserLoginForm(request.POST)
    if form.is_valid():
      print ("получены данные <form> авторизации")
      form.save()
      # cleaned data is a dictionary
      username = form.cleaned_data.get('username')
      messages.success(request, f"{username}, ваша учетная запись создана, пожалуйста, войдите в систему.")
      return redirect('authorization')
  else:
    form = UserLoginForm()
  return render(request, 'recipe_app/login.html', {'form': form})

@login_required()
def profile(request):
  return render(request, 'recipe_app/profile.html')