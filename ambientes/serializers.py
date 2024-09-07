from rest_framework import serializers
from .models import TipoAmbiente, Ambiente, Equipo, DetalleAmbienteEquipo

class TipoAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAmbiente
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class DetalleAmbienteEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleAmbienteEquipo
        fields = '__all__'
