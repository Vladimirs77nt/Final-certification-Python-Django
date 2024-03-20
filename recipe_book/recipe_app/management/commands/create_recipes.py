from datetime import date
import random
from django.core.management.base import BaseCommand
from recipe_app.models import Recipe, Author, Category

class Command(BaseCommand):
    help = "Создание случайных {count} рецептов"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество рецептов')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
            # count - количество создаваемых категорий
        
        recipes_name = ['Тыквенный пирог', 'Хлебный омлет', 'Макароны бантики', 'Гуфи Гискарбинка (The Sims)',
                       'Выпечка', 'Пирог со сливочным сыром', 'Пирог со сливочным сыром', 'Пирог со сливочным сыром',
                       'Пирог со сливочным сыром', 'Пирог со сливочным сыром', 'Ризотто с овощами', 'Налетайка (Genshin Impact)',
                       'Брускетта с крабом', 'Оссобуко', 'Макароны ракушки', 'Джелато',
                       'Йогурт с манго и семенами чиа', 'Сливочные пряники', 'Маслины', 'Шоколад с солёными крекерами',
                       'Фруктовый лёд', 'Говяжьи ребра с овощным рататуем', 'Невесомый блинчик (Genshin Impact)', 'Онигири с мисо-пастой',
                       'Цветочный мёд', 'Блинчики с курицей и грибами', 'Пицца с салями и моцареллой', 'Блины со сливочным мороженым и мармеладом',
                       'Пицца-роллы с ананасом (Domino’s Pizza)', 'Оладьи из цукини', 'Печенье с кокосом', 'Джем из яблок']
        
        authors = Author.objects.all()
        categories = Category.objects.all()

        for i in range(count):
            recipe_name = random.choice(recipes_name)
            recipes_name.remove(recipe_name)

            author = random.choice(authors)
            print (author)
            category = random.choice(categories)

            recipe = Recipe(author = author,
                            title = recipe_name,
                            description = "какое-то описание рецепта",
                            ingredients = "инградиенты: 1, 2, 3....",
                            steps_cooking = "шаги приготовления: 1, 2, 3....",
                            time_for_cooking = f'{random.randint(2,16)*5}',
                            categories = category,
                            )
            recipe.save()
            print(f'Create recipe: {recipe}')
        self.stdout.write(f'Всего: {count} рецептов создано')