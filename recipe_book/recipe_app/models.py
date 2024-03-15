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
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    about = models.TextField()
    birthday = models.DateField()
    
    def __str__(self):
        return self.name

"""
---------------------------------------------------------------------------------
модель «Категория» (Category):
    — name: название категории
    — description: описание категории
"""
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}'

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
    title = models.CharField(max_length=64)
    description = models.TextField()
    ingredients = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField()
    photo = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_add = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return f'{self.title} ({self.author})'

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