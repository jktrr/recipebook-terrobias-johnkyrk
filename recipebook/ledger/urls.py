from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', views.index, name='redirect'),
]

app_name = 'ledger'
