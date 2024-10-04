from django.urls import path, include

urlpatterns = [
    path('api/', include('gestion_emploi_du_temps.urls')),
]