"""CommerceCustomer Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_many


class CommerceCustomer(Model, SoftDeletesMixin):
    """CommerceCustomer Model."""

    __fillable__ = ["name", "email", "password", "phone"]
    __hidden__ = ["password"]
    __auth__ = "email"

    @has_many("id", "customer_id")
    def comments(self):
        """Returns all comments."""
        from .CommerceComment import CommerceComment
        return CommerceComment