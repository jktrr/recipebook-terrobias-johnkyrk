from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ledger.urls'), name='index'),
    path('admin/', admin.site.urls),
    path('recipes/', include('ledger.urls'), name='list'),
    path('recipe/', include('ledger.urls'), name='recipe'),
]
