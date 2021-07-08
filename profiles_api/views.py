from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, put, patch, delete)',
            'Is similar to traditional Django view',
            'Gives you most control over your application logic',
            'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def put(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    