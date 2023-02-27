"""CommerceAttribute Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many

class CommerceAttribute(Model):
    """CommerceAttribute Model."""

    __table__ = "commerce_attributes"
    __primary_key__ = "id"

    __fillable__ = ["title", "status"]

    @belongs_to_many(
        local_foreign_key="attribute_id",
        other_foreign_key="product_id",
        table="commerce_product_attribute",
    )
    def products(self):
        """Returns all products for this attribute."""
        from ..models.CommerceProduct import CommerceProduct
        return CommerceProduct