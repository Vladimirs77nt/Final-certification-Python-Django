from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Category, Recipe

class AuthorForm (forms.ModelForm):
    class Meta:
        model = Author
        # исключаемые поля
        exclude = []
        # названия полей
        labels = {'name': 'Имя',
                  'email': 'Электронная почта',
                  'about': 'О себе',
                  'birthday': 'День рождения',
                  'date_reg': 'Дата регистрации',
                  }
        
class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = Author
    fields = ['username', 'email', 'password1', 'password2']
    # названия полей
    labels = {'username': 'Логин'}

class UserLoginForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = Author
    fields = ['username', 'email', 'password1']
    # названия полей
    labels = {'username': 'Логин'}

class RecipeForm (forms.ModelForm):
    class Meta:
        model = Recipe

        # исключаемые поля
        exclude = []

        # названия полей
        labels = {'title': 'Рецепт',
                  'description': 'Краткое описание',
                  'ingredients': 'Ингредиенты для приготовления',
                  'steps_cooking': 'Шаги приготовления',
                  'aboutime_for_cookingt': 'Время приготовления',
                  'photo': 'Фото блюда',
                  'author': 'Автор',
                  }
        
class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category

        # исключаемые поля
        exclude = []

        # названия полей
        labels = {'name': 'Категория',
                  'description': 'Краткое описание',
                  }