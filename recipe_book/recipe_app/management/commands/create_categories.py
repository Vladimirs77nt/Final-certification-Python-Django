from datetime import date
import random
from django.core.management.base import BaseCommand
from recipe_app.models import Category
import faker    # генерация фейковых имен

class Command(BaseCommand):
    help = "Создание категорий рецептов"

    def handle(self, *args, **kwargs):
        categories = ['Салаты', 'Супы', 'Каши', 'Мясные', 'Выпечка']
        count = 0
        for i_category in categories:
            category = Category(name=i_category,
                                description='какое-то описание категории, бла-бла-бла',
                                )
            category.save()
            print(f'Create category: {category}')
            count += 1
        self.stdout.write(f'Всего: {count} категорий создано')