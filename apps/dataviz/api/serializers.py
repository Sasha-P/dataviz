from rest_framework import serializers

from ..models import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name', 'value')


class RegionSerializer(serializers.Serializer):
    region = serializers.CharField()
