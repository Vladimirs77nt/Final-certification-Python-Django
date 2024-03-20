import random
from django.db import models

"""
---------------------------------------------------------------------------------
модель Автор (Author):
    ○ name: имя - до 64 символов
    ○ email: электронная почта автора
    ○ about: немного о себе (об авторе)
    ○ birthday: день рождения автора
"""
class Author(models.Model):
    username = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    about = models.TextField()
    birthday = models.DateField()
    date_reg = models.DateField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    set_password = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

"""
---------------------------------------------------------------------------------
модель «Категория» (Category):
    — name: название категории
    — description: описание категории
"""
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

"""
---------------------------------------------------------------------------------
модель «Рецепт» (Recipe):
    — title: название рецепта
    — description: описание рецепта
    — ingredients: ингредиенты для приготовления
    — steps_cooking: шаги приготовления
    — time_for_cooking: время приготовления
    — photo: фото приготовленного блюда
    — author: автор (связь с моделью Author)
    — date_add: дата добавления рецепта
    
"""
class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    ingredients = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField()
    photo = models.ImageField()
    date_add = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} ({self.author})'
    
    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:12])}...'

"""
---------------------------------------------------------------------------------
Связующая модель «Записи» (Records):
    — связь с моделью «Рецепт», указывает на рецепты, относящиеся к определенной категории
    — связь с моделью «Категория», указывает на категории привязанные к рецепту

"""
class Records(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_record = models.DateField()

    def __str__(self):
        return f'{self.category} {self.recipe}'
    
"""
---------------------------------------------------------------------------------
модель Комментарий (к рецепту).
Авторы могут добавлять комментарии к своим и чужим рецептам.
Т.е. у комментария может быть один автор. И комментарий относится к одному рецепту.
У модели следующие поля:
    ○ автор
    ○ рецепт
    ○ комментарий
    ○ дата создания

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_create = models.DateField(auto_now_add=True)
    
    def __str__(self):
        words = self.content.split()
        return f'Комментарий [{self.pk}], рецепт: {self.recipe.title} | автор: {self.author.name} |  комментарий: {" ".join(words[:8])}...'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
"""