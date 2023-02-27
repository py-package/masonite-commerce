from src.masonite_commerce.models.CommerceTag import CommerceTag

from .base_query import BaseQuery


class TagQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__()

        self.query = CommerceTag().get_builder()

    def where_title(self, title: str):
        """Filters a category by title"""
        if title:
            self.query.where("title", "like", f"%{title}%")

        return self
