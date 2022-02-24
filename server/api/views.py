from .models import BuzzList
from api.permissions import IsOwnerOrReadOnly
from api.serializers import BuzzListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class BuzzListIndexView(APIView):
    """
    Views for creating a post
    """

    def get(self, request, format=None):
        owned_buzz_lists = BuzzList.objects.filter(owner=request.user)
        serializer = BuzzListSerializer(owned_buzz_lists, many=True)
        return Response(serializer.data)

