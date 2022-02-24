from django.conf import settings
from api.models import BuzzList
from rest_framework.serializers import ModelSerializer


class BuzzListSerializer(ModelSerializer):
    class Meta:
        model = BuzzList
        fields = ['id', 'created', 'changed', 'name', 'slug', 'owner']

class UserSerializer(ModelSerializer):
  class Meta:
    model = settings.AUTH_USER_MODEL
    fields = ('username', 'email', 'id')