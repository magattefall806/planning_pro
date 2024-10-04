from django.urls import path
from . import views

urlpatterns = [
    path('departements/', views.departement_list),
    path('departements/<int:pk>/', views.departement_detail, name='departement_detail'),
    path('metiers/', views.metier_list),
    path('metiers/<int:pk>/', views.metier_detail, name='metier_detail'),
]