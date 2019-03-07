from .views import FlightViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flight_info', FlightViewSet)
urlpatterns = router.urls
