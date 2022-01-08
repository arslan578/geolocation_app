from rest_framework.serializers import ModelSerializer
from home.models import GeoLocation


class GeoLocationModelSerializer(ModelSerializer):
    class Meta:
        model = GeoLocation
        exclude = ['address', 'created_at', 'updated_at']
