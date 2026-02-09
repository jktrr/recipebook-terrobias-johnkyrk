from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list', views.recipe_list, name='recipe_list'),
    path('<int:num>', views.index, name='index'),
    path('', views.default, name='redirect'),
]

app_name = 'ledger'