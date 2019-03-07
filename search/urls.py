from django.conf.urls import url, include
from .views import GetSearchView, GetFilterView


urlpatterns = [
    url(r'^get_flight_data_by_search/', GetSearchView.as_view()),
    url(r'^get_flight_data_by_filter/', GetFilterView.as_view()),
]