from rest_framework import serializers
from .models import pais_capital

class PaisCapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = pais_capital
        fields = ('id', 'pais', 'capital')