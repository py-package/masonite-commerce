# flake8: noqa: E501
"""CreateCommerceCategoryProductTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceCategoryProductTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_category_product") as table:
            table.increments("id")
            table.integer("category_id").unsigned()
            table.foreign("category_id").references("id").on("commerce_categories").on_delete(
                "cascade"
            )
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete(
                "cascade"
            )
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_category_product")
