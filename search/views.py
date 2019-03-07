from django.http import HttpResponse
from django.db.models import Q
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
            source_destination = request.GET.get("source_destination")
            end_destination = request.GET.get("end_destination")
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            flight_details = JourneyInfo.objects.filter(Q(flight_route__start_location=source_destination)| 
                                                        Q(flight_route__end_location=end_destination)| 
                                                        Q(flight_route__start_time__date=start_date)|
                                                        Q(flight_route__end_time__date=end_date)|
                                                        Q(flight__msn=request.GET.get('msn'))|
                                                        Q(flight_route__flight_number=request.GET.get("flight_number"))|
                                                        Q(flight__flight_aircraft_id=request.GET.get('flight_id')))

                                                        
            serializer = DataSerializer(flight_details, many=True)
            return Response({"success": True, "data": serializer.data})
        except Exception as e:
            return Response({"success": False, "message": "Something Went Wrong " + str(e)})
