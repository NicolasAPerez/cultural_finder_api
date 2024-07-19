from rest_framework import serializers

from locations.models import Location, Rating


class LocationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location_name', 'address', 'city', 'picture', 'description', 'average_score', 'total_ratings']


class LocationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name', 'address', 'city', 'description']


class FeaturedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location_name', 'average_score']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['location', 'number_stars']
