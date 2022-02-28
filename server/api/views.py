from .models import Template
from api.serializers import TemplateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)


class TemplateList(ListAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class TemplateCreate(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class TemplateDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class VehicleList(ListAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class VehicleCreate(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class VehicleDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
