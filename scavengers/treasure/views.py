import json
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Treasure
from django.db import models


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
