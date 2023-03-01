from src.masonite_commerce.models.CommerceCustomer import CommerceCustomer

from .base_query import BaseQuery


class CustomerQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__()

        self.query = CommerceCustomer().get_builder()

    def where_name(self, name: str):
        """Filters a category by name"""
        if name:
            self.query.where("name", "like", f"%{name}%")

        return self
