# views.py
from django.shortcuts import render
from .forms import FarePredictionForm
from .utils import predict_fare

def predict_view(request):
    if request.method == 'POST':
        form = FarePredictionForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            distance = form.cleaned_data['distance']
            bearing = form.cleaned_data['bearing']
            fare = predict_fare(year, distance, bearing)
            return render(request, '/Users/mac/Documents/Django_deployment/django_model/django_model_app/templates/result.html', {'fare': fare})
    else:
        form = FarePredictionForm()
    return render(request, '/Users/mac/Documents/Django_deployment/django_model/django_model_app/templates/predict.html', {'form': form})
