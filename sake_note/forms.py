from django import forms
from .models import Sake

class SakeForm(forms.ModelForm):
    class Meta:
        model = Sake
        fields = ['title', 'brewery', 'score', 'tasting_date', 'image',  'memo']
        widgets={
            "tasting_date": forms.NumberInput(attrs={"type":"date"}),
        }
