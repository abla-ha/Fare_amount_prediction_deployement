# fare_prediction/forms.py
from django import forms

class FarePredictionForm(forms.Form):
    year = forms.IntegerField(label='Year', min_value=2000, max_value=2100)
    distance = forms.FloatField(label='Distance (in km)')
    bearing = forms.FloatField(label='Bearing (in degrees)')