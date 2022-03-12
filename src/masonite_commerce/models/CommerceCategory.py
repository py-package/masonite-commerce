"""CommerceCategory Model."""
from masoniteorm.models import Model


class CommerceCategory(Model):
    """CommerceCategory Model."""

    __table__ = "commerce_categories"
    
    __fillable__ = ["parent_id", "title", "slug", "status"]
