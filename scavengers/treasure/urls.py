from django.urls import path    
from . import views
from .views import TreasureCreateView


urlpatterns = [
    path("", views.index, name="treasure_index"),
    path('search/', views.search_view, name='treasure_search'),
    path('create/', TreasureCreateView.as_view(), name='treasure_create'),
]
