from api.models import Note
from api.serializers import NoteSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class NoteList(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
