from django.db import models

"""
---------------------------------------------------------------------------------
модель Автор (Author):
    ○ name: имя - до 64 символов
    ○ surname: фамилия - до 64 символов
    ○ fullname: полное "имя/фамилия" - до 64 символов
    ○ email: электронная почта автора
    ○ telephone: номер телефона автора (символьное поле!)
    ○ about: немного о себе (об авторе)
    ○ birthday: день рождения автора
    ○ photo: фото автора
"""
class Author(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    fullname = models.CharField(max_length=128, default='')
    email = models.EmailField()
    telephone = models.CharField(max_length=24)
    about = models.TextField()
    birthday = models.DateField()
    photo = models.ImageField()
    
    def save (self, *args, **kwargs):
        self.fullname = f"{self.surname} {self.name}"
        super().save (*args, **kwargs)

    def __str__(self):
        return f'{self.fullname}'

"""
---------------------------------------------------------------------------------
модель «Категория» (Category):
    — name: название категории
    — description: описание категории
"""
class Category(models.Model):
    name = models.CharField(max_length=64)
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
    ingredients = models.CharField(max_length=128)
    steps_cooking = models.TextField()
    time_for_cooking = models.TimeField()
    photo = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_add = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}, time: {self.time_for_cooking}, author: {self.author.fullname}'

"""
---------------------------------------------------------------------------------
Связующая модель «Записи» (Records):
    — связь с моделью «Автор», указывает на автора, написавшего рецепт
    — связь с моделью «Рецепт», указывает на рецепты, написанный этим автором

"""
class Order(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    recipe = models.ManyToManyField(Recipe)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField()

    def __str__(self):
        text_out = f'{self.client.name}, date ordered: {self.date_ordered}:\n'
        products_in_order = self.products.all()
        for i_product in products_in_order:
            text_out += f" > {i_product.name}, price: {i_product.price}\n"
        text_out += f' total_price: {self.total_price}'
        return f'Order [id: {self.pk}] {text_out}'