from django.db import models
from django.core.exceptions import ValidationError

class TipoAmbiente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ambiente(models.Model):
    codigo = models.CharField(max_length=20, unique=True, default='TEMP_CODE_Ambiente')  # Código único
    tipo_ambiente = models.ForeignKey(TipoAmbiente, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.codigo

    # Validación para asegurarse de que la capacidad no sea negativa
    def clean(self):
        if self.capacidad < 0:
            raise ValidationError("La capacidad no puede ser negativa.")

class Equipo(models.Model):
    codigo = models.CharField(max_length=20, unique=True, default='TEMP_CODE_Equipo')  # Código único
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    caracteristicas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} ({self.nombre})"

class DetalleAmbienteEquipo(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        # Evitar duplicación de la misma combinación de ambiente y equipo
        unique_together = ('ambiente', 'equipo')

    def __str__(self):
        return f"{self.cantidad} x {self.equipo.codigo} en {self.ambiente.codigo}"

    # Validación para asegurarse de que la cantidad no sea negativa
    def clean(self):
        if self.cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")

