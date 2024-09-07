from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoAmbiente, Ambiente, Equipo, DetalleAmbienteEquipo
from .serializers import TipoAmbienteSerializer, AmbienteSerializer, EquipoSerializer, DetalleAmbienteEquipoSerializer

class TipoAmbienteViewSet(viewsets.ModelViewSet):
    queryset = TipoAmbiente.objects.all()
    serializer_class = TipoAmbienteSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class DetalleAmbienteEquipoViewSet(viewsets.ModelViewSet):
    queryset = DetalleAmbienteEquipo.objects.all()
    serializer_class = DetalleAmbienteEquipoSerializer

