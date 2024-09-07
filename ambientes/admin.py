from django.contrib import admin
from .models import TipoAmbiente, Ambiente, Equipo, DetalleAmbienteEquipo

admin.site.register(TipoAmbiente)
admin.site.register(Ambiente)
admin.site.register(Equipo)
admin.site.register(DetalleAmbienteEquipo)

