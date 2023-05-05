from rest_framework import routers
from .api import PaisCapitalViewSet

router = routers.DefaultRouter()
router.register('api/pais_capital', PaisCapitalViewSet, 'pais_capital')

#Se exporta el urlPatterns
urlpatterns = router.urls