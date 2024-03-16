from django.contrib import admin
from .models import Category, Recipe, Author

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'time_for_cooking', 'date_add']
    ordering = ['title', 'author', 'time_for_cooking', 'date_add']
    list_filter = ['author', 'time_for_cooking', 'date_add']
    search_fields = ['title', 'description']
    search_help_text = 'Поиск по полям Title и Description'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'about', 'birthday']
    ordering = ['name', 'about', 'birthday']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)