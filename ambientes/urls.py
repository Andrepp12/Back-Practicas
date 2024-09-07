from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoAmbienteViewSet, AmbienteViewSet, EquipoViewSet, DetalleAmbienteEquipoViewSet

router = DefaultRouter()
router.register(r'tipo-ambiente', TipoAmbienteViewSet)
router.register(r'ambiente', AmbienteViewSet)
router.register(r'equipo', EquipoViewSet)
router.register(r'detalle-ambiente-equipo', DetalleAmbienteEquipoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
