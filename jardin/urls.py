from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/<int:seccion_id>/', views.galeria_seccion, name='galeria_seccion'),
]

