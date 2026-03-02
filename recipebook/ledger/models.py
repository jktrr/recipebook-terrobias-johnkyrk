from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    bio = models.TextField(validators=[MinLengthValidator(255)])

    def __str__(self):
        return self.user
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('ledger:recipe_detail', args=[str(self.name)])    
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='task_list', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_list', args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")