from django.contrib import admin
from .models import Category, Recipe, Author

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Author)