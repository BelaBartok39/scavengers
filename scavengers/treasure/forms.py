from django import forms
from .models import Treasure

class TreasureCreationForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'description', 'hints', 'image', 'longitude', 'latitude']
        
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)