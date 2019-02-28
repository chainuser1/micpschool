from django import forms
from .models import CarouselIndex

class CarouselIndexForm(forms.ModelForm):
    class Meta:
        model = CarouselIndex
        fields = ('title', 'file', 'description' )