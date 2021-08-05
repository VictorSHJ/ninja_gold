from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    #path('/', views.index),
    path('calcular', views.calcular),
    path('limpiar', views.resetear),
]
