"""CommerceOrderDetail Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class CommerceOrderDetail(Model):
    """CommerceOrderDetail Model."""

    __table__ = "commerce_orders"
    __primary_key__ = "id"

    __fillable__ = ["order_id", "product_id", "product_variation_id", "quantity", "price", "discount", "tax", "total"]

    @belongs_to("order_id", "id")
    def order(self):
        """Returns the order."""
        from .CommerceOrder import CommerceOrder
        return CommerceOrder
    
    @belongs_to("product_id", "id")
    def order(self):
        """Returns the production."""
        from .CommerceProduct import CommerceProduct
        return CommerceProduct
    
    @belongs_to("product_variation_id", "id")
    def order(self):
        """Returns the production variation."""
        from .CommerceProductVariation import CommerceProductVariation
        return CommerceProductVariation
    