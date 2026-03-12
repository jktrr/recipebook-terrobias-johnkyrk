from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy


def index(request):
    return redirect('/accounts/login/')


class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = ''


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('ledger:recipe_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.profile = Profile.objects.get(user=request.user)
            recipe.save()
            return redirect(self.success_url)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'add_image.html'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeImageForm()
        context['recipe_pk'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
            image.save()
            return redirect('ledger:recipe_detail', pk=self.kwargs['pk'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
