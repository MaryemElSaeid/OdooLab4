from django import forms
from .models import Itinew

class ItinewForm(forms.ModelForm):
    class Meta:
        model = Itinew
        fields = "__all__"
