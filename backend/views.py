from backend.models import ErrorCode
from rest_framework import viewsets
from backend.serializers import ErrorCodeSerializer


class ErrorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ErrorCode.objects.all()
    serializer_class = ErrorCodeSerializer