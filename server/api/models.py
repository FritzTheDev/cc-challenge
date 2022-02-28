from django.conf import settings
from django.db.models import (
    Model,
    CharField,
    TextChoices,
    DateTimeField,
    ForeignKey,
    CASCADE,
)
from django.forms import BooleanField
from django.utils.translation import gettext_lazy as _


class Template(Model):
    """
    Basically just a markdown document that gets combined with vehicle names to generate posts.
    """

    # Metadata
    created = DateTimeField(auto_now_add=True, editable=False)
    changed = DateTimeField(auto_now=True)

    # Main Data
    title = CharField(max_length=255)
    slug = CharField(max_length=255)
    markdown = CharField(max_length=20000)
    published = BooleanField(default=False)

    # Template Author - Only for internal record-keeping
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class Vehicle(Model):
    """
    A vehicle with make + model + other info. Used in combination with a vehicle template to generate posts
    """

    # Vehicle Type Choices
    class VehicleTypes(TextChoices):
        CAR = ("CAR", _("Car"))
        VAN = ("VAN", _("Van"))
        TRUCK = ("TRU", _("Truck"))
        SUV = ("SUV", _("SUV"))

    # Metadata
    created = DateTimeField(auto_now_add=True, editable=False)
    changed = DateTimeField(auto_now=True)

    # Main Data
    make = CharField(max_length=50)
    model = CharField(max_length=50)
    image_url = CharField(max_length=255)
    type = CharField(max_length=3, choices=VehicleTypes.choices)
