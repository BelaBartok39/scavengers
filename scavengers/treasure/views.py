from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm
from .models import treasure


def index(request):

    if request.method == 'POST':
        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, "treasure/base.html", {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, "treasure/base.html", {'form': form})

def get_marker_data(request):
    treasures = treasure.objects.all()
    marker_data = [
        {
            'latitude': treasure.latitude,
            'longitude': treasure.longitude,
            'name': treasure.name
        }
        for treasure in treasures
    ]
    return JsonResponse(marker_data, safe=False)



