"""CreateCommerceProductTagTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceProductTagTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_product_tag") as table:
            table.increments("id")
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete(
                "cascade"
            )
            table.integer("tag_id").unsigned()
            table.foreign("tag_id").references("id").on("commerce_tags").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_product_tag")
