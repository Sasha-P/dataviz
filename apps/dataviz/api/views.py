from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Country
from .serializers import CountrySerializer, RegionSerializer


class RegionGet(APIView):
    serializer_class = RegionSerializer

    def post(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        serializer.is_valid()
        region = serializer.validated_data['region']
        countrys = Country.objects.filter(region__name=region).order_by('name')
        countrys_serializer = CountrySerializer(countrys, many=True)
        return Response(countrys_serializer.data)
