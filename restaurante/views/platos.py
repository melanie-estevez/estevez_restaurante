from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from restaurante.models import Plato
from restaurante.serializers import PlatoSerializer
from restaurante.permissions import IsStaffOrReadOnly
from restaurante.filters import PlatoFilter


class PlatoViewSet(ModelViewSet):
    queryset = Plato.objects.select_related('categoria').all()
    serializer_class = PlatoSerializer

    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = PlatoFilter

    search_fields = [
        'nombre',
        'descripcion',
        'categoria__nombre',
    ]

    ordering_fields = [
        'id',
        'nombre',
        'precio',
    ]

    ordering = [
        'nombre',
    ]