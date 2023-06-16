from django.contrib import admin
from .models import Treasure

# Register your models here.

admin.site.register(Treasure)

admin.site.site_header = "Scavenger Admin"
admin.site.site_title = "Scavenger Admin Portal"
admin.site.index_title = "Welcome to Scavenger Portal"