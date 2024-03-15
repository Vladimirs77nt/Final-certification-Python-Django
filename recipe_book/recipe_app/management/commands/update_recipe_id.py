from django.core.management.base import BaseCommand
from recipe_app.models import Recipe

class Command(BaseCommand):
    help = "Update recipe time by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Recipe ID')
        parser.add_argument('time', type=str, help='Time for cooking')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        time = kwargs.get('time')
        recipe = Recipe.objects.filter(pk=pk).first()
        recipe.time_for_cooking = time
        recipe.save()
        self.stdout.write(f'{recipe}')