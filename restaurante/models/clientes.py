from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cliente',
        null=True,
        blank=True
    )

    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo