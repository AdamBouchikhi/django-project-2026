from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_drag, name='calculate_drag'),
]

