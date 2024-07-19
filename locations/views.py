from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from locations.models import Location
from locations.serializers import *


class LocationGetAPI(APIView):

    def get(self, request, pk, format=None):
        data = LocationReadSerializer(get_object_or_404(Location, pk=pk))
        return Response(data.data)


class LocationAllAPI(APIView):

    def get(self, request, format=None):
        featured = Location.objects.all().annotate(average_score=Avg('rating__number_stars')).order_by('-average_score')
        serializer = FeaturedLocationSerializer(featured, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serial = LocationWriteSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationCityAPI(APIView):

    def get(self, request, city, format=None):
        related = Location.objects.filter(city__iexact=city).annotate(average_score=Avg('rating__number_stars')).order_by('-average_score')
        serializer = FeaturedLocationSerializer(related, many=True)
        return Response(serializer.data)


class RatingAPI(APIView):

    def post(self, request):
        serial = RatingSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)




