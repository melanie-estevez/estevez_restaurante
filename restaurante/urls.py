from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from restaurante.views.health import health_check
from restaurante.views.auth import RegisterView, LogoutView
from restaurante.views.user import UserViewSet
from restaurante.views.clientes import ClienteViewSet
from restaurante.serializers.auth import CustomTokenView
from restaurante.views.category import CategoriaMenuViewSet
from restaurante.views.platos import PlatoViewSet
from restaurante.views.pedidos import PedidoViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('categorias', CategoriaMenuViewSet,  basename='category')
router.register('platos', PlatoViewSet, basename='plato')
router.register('pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('health/', health_check),

    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('auth/logout/', LogoutView.as_view()),

    path('', include(router.urls)),
]