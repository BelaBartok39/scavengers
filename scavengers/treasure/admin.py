from django.contrib import admin
from .models import treasure

# Register your models here.

admin.site.register(treasure)

admin.site.site_header = "Scavenger Admin"
admin.site.site_title = "Scavenger Admin Portal"
admin.site.index_title = "Welcome to Scavenger Portal"