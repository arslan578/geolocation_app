from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from home.api.v1.serializers import GeoLocationModelSerializer
from home.models import GeoLocation
from geopy.geocoders import Nominatim


class GeoLocationViewSet(ViewSet):
    serializer_class = GeoLocationModelSerializer

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            geo_locator = Nominatim(user_agent=settings.GOOGLE_DEVELOPER_APP_ACCOUNT_NAME)
            coordinates = "{}, {}".format(serializer.validated_data['latitude'], serializer.validated_data['longitude'],
                                          )
            location = geo_locator.reverse(coordinates)
            geo_location = GeoLocation(username=serializer.validated_data['username'],
                                       latitude=serializer.validated_data['latitude'],
                                       longitude=serializer.validated_data['longitude'],
                                       address=location.address)

            geo_location.save()

            status = HTTP_200_OK

        except Exception as e:
            status = HTTP_400_BAD_REQUEST

        return Response(status=status)
