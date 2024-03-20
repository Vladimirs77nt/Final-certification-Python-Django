from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_all/', views.recipe_all, name='recipe_all'),
    path('author_all/', views.author_all, name='author_all'),
    path('users/', include('users.urls', namespace='users')),

    path('recipe/<int:recipe_id>/', views.recipe_id, name='recipe_id'),
    path('author/<int:author_id>/', views.author_id, name='author_id'),

    path('registration/', views.registration, name="registration"),
    path('authorization/', views.authorization, name='authorization'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)