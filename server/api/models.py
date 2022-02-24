from django.conf import settings
from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE
from django.forms import BooleanField


class BuzzList(Model):
    """
    Roughly Equivalent To An "Organization".
    - Billing takes place at this level.
    - Each List has one Owner & 0-N Staff based on tier.
    - Owners and staff can be associated with multiple lists.
    - Owners have full access to their list. Each staff member has configurable access.
    - Lists can have any number of subscribers.
    - Lists can have sublists of subscribers.
    """

    # Metadata
    created = DateTimeField(auto_now_add=True, editable=False)
    changed = DateTimeField(auto_now=True)

    # Organization Name
    name = CharField(max_length=50)
    slug = CharField(max_length=50)

    # Relationships
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class StaffMembership(Model):
    """
    Staff Memberships are a membership object relating users & lists.
    Staff Memberships include permission settings for their associated list.
    Permissions include:
    - View List (Read)
    - Manage Members (Create/Update/Delete)
    - Send Texts (Create)
    - Manage List (Update)
    """

    created = DateTimeField(auto_now_add=True, editable=False)
    changed = DateTimeField(auto_now=True)

    # Permissions
    view_list = BooleanField()
    manage_members = BooleanField()
    send_texts = BooleanField()
    manage_list = BooleanField()

    # Relationships
    buzz_list = ForeignKey(BuzzList, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
