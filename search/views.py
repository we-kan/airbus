from django.http import HttpResponse
from rest_framework.response import Response
from flight.models import Flight
from flight_route.models import JourneyInfo
from .serializers import DataSerializer

from rest_framework.views import APIView


class GetSearchView(APIView):
    """

    """
    def get(self, request):
        """
        ---
        parameters:
            - name: msn
              required: false
              paramType: query
            - name: flight_number
        """
        flight_details = []
        try:
            msn = request.GET.get("msn")
            flight_number = request.GET.get("flight_number")

            if not msn and not flight_number:
                return Response({"success": False, "message": "Give either msn or flight number"})
            if not flight_number:
                flight_details = JourneyInfo.objects.filter(flight__msn=request.GET.get("msn"))
            if not msn:
                flight_details = JourneyInfo.objects.filter(flight_route__flight_number=flight_number)
            else:
                flight_details = JourneyInfo.objects.filter(flight__msn=request.GET.get("msn"), flight_route__flight_number=flight_number)
            serializer = DataSerializer(flight_details, many=True)
            return Response({"success": True, "data": serializer.data})

        except Exception as e:
            return Response({"success": False, "message": "Something Went Wrong " + str(e)})


class GetFilterView(APIView):
    """

    """
    def get(self, request):
        """
        ---
        parameters:
            - name: journey_dates
              required: false
              paramType: query
            - name: source_destinations
            - name: end_destinations

        """
        flight_details = []
        try:
            dates = request.GET.get("journey_dates")
            source_destination = request.GET.get("source_destination")
            end_destination = request.GET.get("end_destination")

            if not dates and not source_destination and not end_destination:
                return Response({"success": False, "message": "Give either dates or destinations"})
            elif not source_destination and not end_destination:
                flight_details = JourneyInfo.objects.filter(journey_date__in=dates)
            elif not dates and not source_destination:
                flight_details = JourneyInfo.objects.filter(flight_route__end_location__in=end_destination)
            elif not dates and not end_destination:
                flight_details = JourneyInfo.objects.filter(flight_route__start_location__in=source_destination)
            elif not dates:
                flight_details = JourneyInfo.objects.filter(flight_route__end_location__in=end_destination, flight_route__start_location__in=source_destination)
            else:
                flight_details = JourneyInfo.objects.filter(flight_route__end_location__in=end_destination, flight_route__start_location__in=source_destination, journey_date__in=dates)
            serializer = DataSerializer(flight_details, many=True)
            return Response({"success": True, "data": serializer.data})

        except Exception as e:
            return Response({"success": False, "message": "Something Went Wrong " + str(e)})
