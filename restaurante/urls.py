from django.urls import path
from . import views

app_name = 'restaurante'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('plato/<int:id>/', views.detalle, name='detalle'),
]