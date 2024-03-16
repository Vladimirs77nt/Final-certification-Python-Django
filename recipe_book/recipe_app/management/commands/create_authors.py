from datetime import date
import random
from django.core.management.base import BaseCommand
from recipe_app.models import Author
import faker    # генерация фейковых имен

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Create Authors (random fake)"

    def handle(self, *args, **kwargs):
        count = 10  # количество создаваемых фейковых авторов
        for i in range(count):
            date_reg = date(year=random.randint(2015,2021), month=random.randint(1,12), day=random.randint(1,30))
            date_birthday = fake.date_between('-70y', '-10y')
            author = Author(name=fake.name(),
                            email=fake.ascii_free_email(),
                            about=f"я {fake.job().lower()}, родом из {fake.city()}",
                            # password=fake.lexify(text='Random Identifier: ??????????'),
                            date_reg=f'{date_reg}',
                            birthday=date_birthday)
            print (i, author)
            print (author.about)
            print (author.birthday)
            author.save()
            self.stdout.write(f'Create author: {author}')
        self.stdout.write(f'Total: {count} author create')