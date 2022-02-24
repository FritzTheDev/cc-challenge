from . import views
from django.urls import path

urlpatterns = [
    path("notes/", views.NoteList.as_view(), name="Note List"),
    path("notes/<int:pk>/", views.NoteDetail.as_view(), name="Note Detail"),
]
