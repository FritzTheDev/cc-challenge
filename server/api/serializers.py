from django.conf import settings
from api.models import Template
from rest_framework.serializers import ModelSerializer


class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = ("id", "created", "title", "slug", "markdown", "published", "author")


class UserSerializer(ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username", "email", "id")
