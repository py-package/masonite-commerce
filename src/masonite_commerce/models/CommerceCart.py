"""CommerceCart Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many, belongs_to


class CommerceCart(Model):
    """CommerceCart Model."""

    __table__ = "commerce_carts"
    __primary_key__ = "id"

    __fillable__ = ["product_id", "customer_id", "quantity"]

    @belongs_to("product_id", "id")
    def product(self):
        """Returns related product for this comment."""
        from ..models.CommerceProduct import CommerceProduct
        return CommerceProduct

    @belongs_to("customer_id", "id")
    def customer(self):
        """Returns related product for this comment."""
        from ..models.CommerceCustomer import CommerceCustomer
        return CommerceCustomer