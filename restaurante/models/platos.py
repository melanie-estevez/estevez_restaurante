from django.db import models


class Plato(models.Model):

    categoria = models.ForeignKey(
        'CategoriaMenu',
        on_delete=models.PROTECT,
        related_name='platos'
    )

    nombre = models.CharField(
        max_length=100
    )

    descripcion = models.TextField(
        blank=True,
        default=''
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    disponible = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre