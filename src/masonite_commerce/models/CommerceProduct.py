"""CommerceProduct Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many, has_one, has_many


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
        from .CommerceCategory import CommerceCategory

        return CommerceCategory

    @has_one("product_id", "id")
    def meta(self):
        """Returns all metas for this product."""
        from .CommerceProductMeta import CommerceProductMeta

        return CommerceProductMeta

    @belongs_to_many(
        local_foreign_key="product_id",
        other_foreign_key="attribute_id",
        table="commerce_product_attribute",
        with_fields=["value"],
    )
    def attributes(self):
        """Returns all attributes for this product."""
        from .CommerceAttribute import CommerceAttribute

        return CommerceAttribute

    @belongs_to_many(
        local_foreign_key="product_id",
        other_foreign_key="tag_id",
        table="commerce_product_tag",
    )
    def tags(self):
        """Returns all tags for this product."""
        from .CommerceTag import CommerceTag
        return CommerceTag

    @has_many("id", "product_id")
    def variations(self):
        """Returns all variations for this product."""
        from .CommerceProductVariation import CommerceProductVariation
        return CommerceProductVariation

    @has_many("id", "product_id")
    def comments(self):
        """Returns all comments for this product."""
        from .CommerceComment import CommerceComment
        return CommerceComment
