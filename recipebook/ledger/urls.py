from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe_list'),
    path('login', views.login_page, name='login'),
    path('<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', views.index, name='redirect'), # only used to automatically bring the user to the list page upon entering the site
]

app_name = 'ledger'