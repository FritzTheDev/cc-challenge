from api.models import Template, Vehicle
from rest_framework.serializers import ModelSerializer


class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = ("id", "created", "changed", "title", "slug", "markdown", "published", "author")

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("id", "created", "changed", "make", "model", "image_url", "type")
