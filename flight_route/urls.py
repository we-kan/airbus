from .views import FlightRouteViewSet, JourneyInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flight_route', FlightRouteViewSet)
router.register(r'journey_info', JourneyInfoViewSet)
urlpatterns = router.urls
