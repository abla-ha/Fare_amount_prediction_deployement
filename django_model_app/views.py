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
            return render(request, 'fare_prediction/result.html', {'fare': fare})
    else:
        form = FarePredictionForm()
    return render(request, 'fare_prediction/predict.html', {'form': form})
