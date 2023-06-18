import json
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.db import models

from .models import Treasure
from django.views.generic import CreateView
from .forms import TreasureCreationForm


class DecimalJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def index(request):
    treasures = Treasure.objects.all()
    treasures_data = []  # List to hold the treasures' data

    # Prepare the treasures' data
    for treasure in treasures:
        treasure_data = {
            'latitude': float(treasure.latitude),
            'longitude': float(treasure.longitude),
            'name': treasure.name,
            'description': treasure.description,
            'hints': treasure.hints,
        }
        treasures_data.append(treasure_data)

    context = {'treasures_data_json': json.dumps(treasures_data, cls=DecimalJSONEncoder)}

    return render(request, "treasure/base.html", context)

def search_view(request):
    query = request.GET.get('search_query')
    treasures = Treasure.objects.filter(
        models.Q(name__icontains=query) | models.Q(zipcode=query) |
        models.Q(city__icontains=query) | models.Q(state__icontains=query)
    )
    return render(request, 'treasure/search_results.html', {'treasures': treasures})

class TreasureCreateView(CreateView):
    model = Treasure
    form_class = TreasureCreationForm
    template_name = 'treasure_create.html'
    success_url = '/treasure/'  # URL to redirect to after successful creation

    def form_valid(self, form):
        # Set the treasure's creator to the current user
        form.instance.creator = self.request.user
        return super().form_valid(form)