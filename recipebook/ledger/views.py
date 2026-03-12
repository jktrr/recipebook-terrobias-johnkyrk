from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return redirect('/accounts/login/')


class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = ''


# class RecipeAddView(LoginRequiredMixin, ListView):
#     model = Recipe
