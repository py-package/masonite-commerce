"""CreateCommerceProductAttributeTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceProductAttributeTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_product_attributes") as table:
            table.increments("id")
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete("cascade")
            table.integer("attribute_id").unsigned()
            table.foreign("attribute_id").references("id").on("commerce_attributes").on_delete("cascade")
            table.string("value")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_product_attributes")
