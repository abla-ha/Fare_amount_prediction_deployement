from django import forms

class FarePredictionForm(forms.Form):
    YEAR_CHOICES = [(year, str(year)) for year in range(2009, 2016)]
    year = forms.ChoiceField(choices=YEAR_CHOICES, label='Year')
    distance = forms.FloatField(widget=forms.HiddenInput(), required=False)
    bearing = forms.FloatField(label='Bearing (in degrees)')
