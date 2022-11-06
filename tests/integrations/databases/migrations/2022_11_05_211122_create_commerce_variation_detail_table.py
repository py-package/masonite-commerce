"""CreateCommerceVariationDetailTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceVariationDetailTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_variation_details") as table:
            table.increments("id")
            table.integer("product_variation_id").unsigned()
            table.foreign("product_variation_id").references("id").on("commerce_product_variations").on_delete(
                "cascade"
            )
            table.integer("product_attribute_id").unsigned()
            table.foreign("product_attribute_id").references("id").on("commerce_product_attribute").on_delete(
                "cascade"
            )
            table.integer("attribute_id").unsigned()
            table.foreign("attribute_id").references("id").on("commerce_attributes").on_delete(
                "cascade"
            )
            table.string("attribute_value").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_variation_details")
