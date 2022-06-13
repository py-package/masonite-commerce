"""CommerceProduct Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many, has_one


class CommerceProduct(Model):
    """CommerceProduct Model."""

    __table__ = "commerce_products"
    __primary_key__ = "id"

    __fillable__ = [
        "creator_id",
        "title",
        "slug",
        "excerpt",
        "content",
        "cover_image",
        "comment_count",
        "comment_status",
        "status",
    ]

    @belongs_to_many(
        local_foreign_key="product_id",
        other_foreign_key="category_id",
        table="commerce_category_product",
    )
    def categories(self):
        """Returns all categories for this product."""
        from ..models.CommerceCategory import CommerceCategory

        return CommerceCategory

    @has_one("product_id", "id")
    def meta(self):
        """Returns all metas for this product."""
        from .CommerceProductMeta import CommerceProductMeta

        return CommerceProductMeta
