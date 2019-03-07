from .views import AirportInfoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'airport', AirportInfoView)
urlpatterns = router.urls
