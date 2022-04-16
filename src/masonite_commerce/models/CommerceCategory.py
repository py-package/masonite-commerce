"""CommerceCategory Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many, has_many, belongs_to


class CommerceCategory(Model):
    """CommerceCategory Model."""

    __table__ = "commerce_categories"
    __primary_key__ = "id"

    __fillable__ = ["creator_id", "parent_id", "title", "slug", "status"]

    @belongs_to_many(
        local_foreign_key="category_id",
        other_foreign_key="product_id",
        table="commerce_category_product",
    )
    def products(self):
        """Returns all products for this category."""
        from ..models.CommerceProduct import CommerceProduct

        return CommerceProduct


    @has_many("id", "parent_id")
    def children(self):
        """Returns all children for this category."""
        from ..models.CommerceCategory import CommerceCategory

        return CommerceCategory


    @belongs_to("parent_id", "id")
    def parent(self):
        """Returns the parent of this category."""
        from ..models.CommerceCategory import CommerceCategory

        return CommerceCategory
