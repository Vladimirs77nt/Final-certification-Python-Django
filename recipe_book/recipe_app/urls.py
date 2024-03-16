from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_all/', views.recipe_all, name='recipe_all'),
    path('author_all/', views.author_all, name='author_all'),

    path('recipe/<int:recipe_id>/', views.recipe_id, name='recipe_id'),
    path('author/<int:author_id>/', views.author_id, name='author_id'),

    path('authorization/', views.authorization, name='authorization'),
    path('registrtion/', views.registrtion, name='registrtion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)