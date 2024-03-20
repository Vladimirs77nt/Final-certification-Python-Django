from datetime import date
import random
from django.core.management.base import BaseCommand
from recipe_app.models import Author
import faker    # генерация фейковых данных

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Создание случайных {count} авторов (модуль Faker)"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество авторов')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
            # count - количество создаваемых категорий
        
        for i in range(count):
            username=f'user_{random.randint(1000,9999)}'
            date_reg = date(year=random.randint(2015,2021), month=random.randint(1,12), day=random.randint(1,30))
            date_birthday = fake.date_between('-70y', '-10y')
            author = Author(name=fake.name(),
                            username=username,
                            email=f'{username}@mail.com',
                            about=f"я {fake.job().lower()}, родом из {fake.city()}",
                            set_password='qwerty123',
                            date_reg=f'{date_reg}',
                            birthday=date_birthday)
            author.save()
            print(f'Create author: {author}')
        self.stdout.write(f'Всего: {count} авторов создано')