from django.db import models


class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        'Pedido',
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    plato = models.ForeignKey(
        'Plato',
        on_delete=models.PROTECT,
        related_name='detalles_pedido'
    )

    cantidad = models.PositiveIntegerField()

    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedido'

    def __str__(self):
        return f'Pedido {self.pedido_id} - {self.plato.nombre}'