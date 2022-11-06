"""CommerceProductVariation Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class CommerceProductVariation(Model):
    """CommerceProductVariation Model."""

    __table__ = "commerce_product_variations"
    __primary_key__ = "id"

    __fillable__ = [
        "product_id",
        "sku",
        "price",
        "min_price",
        "max_price",
        "on_sale",
        "stock_quantity",
        "stock_status",
        "total_sales",
        "image"
    ]

    __casts__ = {
        "price": "float",
        "min_price": "float",
        "max_price": "float",
        "average_rating": "float"
    }

    @belongs_to
    def product(self):
        """Returns the product for this meta."""
        from .CommerceProduct import CommerceProduct
        return CommerceProduct

    @has_many("id", "product_variation_id")
    def details(self):
        """Returns all variation details"""
        from .CommerceProductVariationDetail import CommerceProductVariationDetail
        return CommerceProductVariationDetail