from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def default(request):
    return redirect('/recipes/list')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'

    def get_queryset(self):
        recipes = self.kwargs.get('recipe')
        return Ingredient.objects.filter(recipe__recipe__name=recipes)