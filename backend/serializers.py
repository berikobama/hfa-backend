from backend.models import HeatingModel, Manufacturer
from rest_framework import serializers


class ErrorCodeSerializer(serializers.Serializer):
    error_code = serializers.CharField()
    description = serializers.CharField()
    solution = serializers.CharField()
    model_name  = serializers.PrimaryKeyRelatedField(queryset=HeatingModel.objects.all())
    manufacturer_name = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    inserted_date = serializers.DateField()
    last_modified_date = serializers.DateField()
