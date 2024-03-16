from django import forms
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
        
class CommentForm (forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Выберите автора")
    content = forms.CharField(widget=forms.Textarea, label="комментарий")