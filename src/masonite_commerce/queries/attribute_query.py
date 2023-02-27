from src.masonite_commerce.models.CommerceAttribute import CommerceAttribute

from .base_query import BaseQuery


class AttributeQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__()

        self.query = CommerceAttribute().get_builder()

    def where_title(self, title: str):
        """Filters a category by title"""
        if title:
            self.query.where("title", "like", f"%{title}%")

        return self
