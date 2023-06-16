import json
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Treasure


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

