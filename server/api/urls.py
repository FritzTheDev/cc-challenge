from . import views
from django.urls import path

urlpatterns = [
    path("lists/", views.BuzzListIndexView.as_view(), name="Buzz List Index"),
]
