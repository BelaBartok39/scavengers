from django.urls import path
from . import views
from .views import get_marker_data


urlpatterns = [
    path("", views.index, name="treasure_index"),
    path('treasure/api/markers/', get_marker_data, name='get_marker_data'),
]