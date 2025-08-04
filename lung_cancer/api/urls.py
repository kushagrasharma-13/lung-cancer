from django.urls import path
from . import views

urlpatterns = [
    path('form-prediction/', views.form_prediction, name='form_prediction'),
    path('image-prediction/', views.image_prediction, name='image_prediction'),
]