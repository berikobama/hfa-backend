from backend.models import ErrorCode
from rest_framework import serializers


class ErrorCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ErrorCode
        fields = '__all__'