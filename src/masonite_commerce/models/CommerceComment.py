"""CommerceComment Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class CommerceComment(Model):
    """CommerceComment Model."""

    __table__ = "commerce_comments"
    __primary_key__ = "id"

    __fillable__ = ["creator_id", "product_id", "content", "star", "status"]

    @belongs_to("product_id", "id")
    def product(self):
        """Returns related product for this comment."""
        from .CommerceProduct import CommerceProduct

        return CommerceProduct

    @belongs_to("parent_id", "id")
    def parent(self):
        """Returns the parent for this comment."""
        from .CommerceComment import CommerceComment

        return CommerceComment
