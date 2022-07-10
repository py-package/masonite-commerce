"""CommerceComment Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class CommerceComment(Model):
    """CommerceComment Model."""

    __table__ = "commerce_comments"
    __primary_key__ = "id"

    __fillable__ = ["creator_id", "product_id", "parent_id", "content", "status"]

    @belongs_to("product_id", "id")
    def products(self):
        """Returns related product for this comment."""
        from ..models.CommerceProduct import CommerceProduct

        return CommerceProduct

    @has_many("id", "parent_id")
    def children(self):
        """Returns all children for this comment."""
        from ..models.CommerceComment import CommerceComment

        return CommerceComment

    @belongs_to("parent_id", "id")
    def parent(self):
        """Returns the parent for this comment."""
        from ..models.CommerceComment import CommerceComment

        return CommerceComment

