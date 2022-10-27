"""CommerceProductMeta Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class CommerceProductMeta(Model):
    """CommerceProductMeta Model."""

    __table__ = "commerce_metas"
    __primary_key__ = "id"

    __fillable__ = [
        "product_id",
        "sku",
        "virtual",
        "downloadable",
        "price",
        "min_price",
        "max_price",
        "on_sale",
        "stock_quantity",
        "stock_status",
        "rating_count",
        "average_rating",
        "total_sales",
        "tax_status",
    ]

    @belongs_to
    def product(self):
        """Returns the product for this meta."""
        from .CommerceProduct import CommerceProduct
        return CommerceProduct
