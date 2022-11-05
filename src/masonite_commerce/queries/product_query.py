from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from .base_query import BaseQuery


class ProductQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__()

        self.query = CommerceProduct().get_builder()
