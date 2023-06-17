from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="treasure_index"),
    path('search/', views.search_view, name='treasure_search'),
]
