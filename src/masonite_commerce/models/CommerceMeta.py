"""CommerceMeta Model."""
from masoniteorm.models import Model


class CommerceMeta(Model):
    """CommerceMeta Model."""

    __table__ = "commerce_metas"
    
    __fillable__ = ["product_id", "sku", "virtual", "downloadable", "min_price", "max_price", "on_sale", "stock_quantity", "stock_status", "rating_count", "average_rating", "total_sales", "tax_status"]
