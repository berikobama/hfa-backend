from backend.models import HeatingModel, Manufacturer, ErrorCode
from rest_framework import serializers


class HeatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatingModel
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ErrorCodeSerializer(serializers.ModelSerializer):
    model_name = HeatingModelSerializer()
    manufacturer_name = ManufacturerSerializer()

    class Meta:
        model = ErrorCode
        fields = '__all__'
