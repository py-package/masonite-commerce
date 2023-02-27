# flake8: noqa F501
"""CreateCommerceOrderDetailsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceOrderDetailsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_order_details") as table:
            table.increments("id")
            table.integer("order_id").unsigned()
            table.foreign("order_id").references("id").on("commerce_orders").on_delete(
                "cascade"
            )
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete(
                "cascade"
            )
            table.integer("product_variation_id").unsigned().nullable()
            table.foreign("product_variation_id").references("id").on("commerce_product_variations").on_delete(
                "set null"
            )
            table.integer("quantity").default(1)
            table.double("price").default(0)
            table.double("discount").default(0)
            table.double("tax").default(0)
            table.double("total").default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_order_details")
