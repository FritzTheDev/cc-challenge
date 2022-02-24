from . import views
from django.urls import path

urlpatterns = [
    path("hello/", views.HelloWorldView.as_view(), name="hello"),
]
