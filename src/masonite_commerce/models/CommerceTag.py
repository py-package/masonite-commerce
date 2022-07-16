"""CommerceTag Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many


class CommerceTag(Model):
    """CommerceTag Model."""

    __table__ = "commerce_tags"
    __primary_key__ = "id"

    __fillable__ = ["title", "slug"]

    @belongs_to_many(
        local_foreign_key="tag_id",
        other_foreign_key="product_id",
        table="commerce_product_tag",
    )
    def products(self):
        """Returns all products for this tag."""
        from ..models.CommerceProduct import CommerceProduct

        return CommerceProduct

