from .auth import CustomTokenSerializer, CustomTokenView
from .user import (
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)
from .clientes import ClienteSerializer
from .category import CategoriaMenuSerializer
from .platos import PlatoSerializer
from .pedidos import PedidoSerializer
from .detalles_pedido import DetallePedidoSerializer