from django.db import models

class Ingredient(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredients")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_name")

