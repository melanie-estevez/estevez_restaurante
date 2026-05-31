from django.db import models


class Pedido(models.Model):

    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PREPARANDO', 'Preparando'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.PROTECT,
        related_name='pedidos'
    )

    fecha_pedido = models.DateTimeField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ['-fecha_pedido']

    def __str__(self):
        return f'Pedido #{self.id}'