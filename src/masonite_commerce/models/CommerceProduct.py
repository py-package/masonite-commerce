"""CommerceProduct Model."""
from masoniteorm.models import Model


class CommerceProduct(Model):
    """CommerceProduct Model."""

    __table__ = "commerce_products"
    
    __fillable__ = ["creator_id", "title", "slug", "excerpt", "content", "cover_image", "comment_count", "comment_status", "status"]
