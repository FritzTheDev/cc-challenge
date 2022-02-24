from django.conf import settings
from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE

# Create your models here.


class Note(Model):
    created = DateTimeField(auto_now_add=True, editable=False)
    changed = DateTimeField(auto_now=True)

    title = CharField(max_length=255)
    body = CharField(max_length=2800)

    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
