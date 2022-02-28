from .views import (
    TemplateCreate,
    TemplateDetail,
    TemplateList,
    VehicleCreate,
    VehicleDetail,
    VehicleList,
)
from django.urls import path

urlpatterns = [
    # Template Routes
    path("template/", TemplateList.as_view(), name="Template List"),
    path("template/create/", TemplateCreate.as_view(), name="Template Create"),
    path("template/<int:pk>/", TemplateDetail.as_view(), name="Template Detail"),
    # Vehicle Routes
    path("vehicle/", VehicleList.as_view(), name="Vehicle List"),
    path("vehicle/create/", VehicleCreate.as_view(), name="Vehicle Create"),
    path("vehicle/<int:pk>/", VehicleDetail.as_view(), name="Vehicle Detail"),
]
