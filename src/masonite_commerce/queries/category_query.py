from src.masonite_commerce.models.CommerceCategory import CommerceCategory
from .base_query import BaseQuery


class CategoryQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__()

        self.query = CommerceCategory().get_builder()
