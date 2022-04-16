"""CommerceAttribute Model."""
from masoniteorm.models import Model


class CommerceAttribute(Model):
    """CommerceAttribute Model."""

    __table__ = "commerce_attributes"
    __primary_key__ = "id"

    __fillable__ = ["title", "status"]
