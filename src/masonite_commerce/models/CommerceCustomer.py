"""CommerceCustomer Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class CommerceCustomer(Model, SoftDeletesMixin):
    """CommerceCustomer Model."""

    __fillable__ = ["name", "email", "password", "phone"]
    __hidden__ = ["password"]
    __auth__ = "email"
