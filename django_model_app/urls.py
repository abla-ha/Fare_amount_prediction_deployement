from django.urls import path
from . import views

urlpatterns = [
    path('prediction/', views.predict_view, name='predict_view'),
    # Other URL patterns
]
