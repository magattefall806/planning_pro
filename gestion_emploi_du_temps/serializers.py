from rest_framework import serializers
from .models import Departement, Metier

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = '__all__'