from .views import TemplateCreate, TemplateDetail, TemplateList
from django.urls import path

urlpatterns = [
    path("template/", TemplateList.as_view(), name="Template Listd"),
    path("template/create/", TemplateCreate.as_view(), name="Template Create"),
    path("template/<int:pk>/", TemplateDetail.as_view(), name="Template Detail"),
]
