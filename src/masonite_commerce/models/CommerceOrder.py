"""CommerceOrder Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import has_many, belongs_to

class CommerceOrder(Model):
    """CommerceOrder Model."""

    __table__ = "commerce_orders"
    __primary_key__ = "id"

    __fillable__ = ["customer_id", "order_date", "shipped_date", "delivered_date", "status", "payment_method", "payment_status", "shipping_method", "is_taxable", "notes"]

    @belongs_to("customer_id", "id")
    def customer(self):
        """Returns the customer."""
        from ..models.CommerceCustomer import CommerceCustomer
        return CommerceCustomer
    
    @has_many("id", "order_id")
    def items(self):
        """Returns all children for this category."""
        from ..models.CommerceOrderDetail import CommerceOrderDetail
        return CommerceOrderDetail