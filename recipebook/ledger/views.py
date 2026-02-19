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
    model = RecipeIngredient
    template_name = 'recipe.html'