from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods',
            'Is similar to',
            'Gives you the most',
            'Is mapped manually',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
