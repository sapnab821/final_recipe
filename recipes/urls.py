from django.urls import path
from . import views
from .views import home, records, RecipeListView, RecipeDetailView, about

app_name = "recipes"

urlpatterns = [
    path('', home, name='home'),  # Homepage view
    path('list/', RecipeListView.as_view(), name='list'),  # URL pattern for showing all recipes
    path('recipes/<pk>/', RecipeDetailView.as_view(), name='detail'),  # URL pattern for recipe detail view
    path('recipes/records/', records, name='records'),
    path('recipes/about/', about, name='about'),
    path('add/', views.add_recipe, name='add_recipe'),
]