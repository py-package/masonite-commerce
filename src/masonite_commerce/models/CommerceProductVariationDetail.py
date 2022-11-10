"""CommerceProductVariationDetail Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class CommerceProductVariationDetail(Model):
    """CommerceProductVariationDetail Model."""

    __table__ = "commerce_variation_details"
    __primary_key__ = "id"

    __fillable__ = [
        "product_variation_id",
        "product_attribute_id",
        "attribute_id",
        "attribute_value",
    ]

    @belongs_to
    def attribute(self):
        """Returns the attribute."""
        from .CommerceAttribute import CommerceAttribute

        return CommerceAttribute

    @belongs_to
    def variation(self):
        """Returns the variation."""
        from .CommerceProductVariation import CommerceProductVariation

        return CommerceProductVariation
