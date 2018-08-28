from backend.models import ErrorCode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.serializers import ErrorCodeSerializer


@api_view(['GET'])
def error_code_list(request):
    if request.method == 'GET':
        queryset = ErrorCode.objects.all()
        serializer = ErrorCodeSerializer(queryset, many=True)
        return Response(serializer.data)
