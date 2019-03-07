from django.conf.urls import url
from .views import AircraftView, AircraftInfoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'aircraft', AircraftView)
router.register(r'aircraft_info', AircraftInfoView)
urlpatterns = router.urls


