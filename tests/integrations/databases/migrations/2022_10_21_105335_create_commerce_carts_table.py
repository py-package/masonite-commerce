# flake8: noqa F501
"""CreateCommerceCartsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceCartsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_carts") as table:
            table.increments("id")
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete("cascade")
            table.integer("customer_id").unsigned()
            table.foreign("customer_id").references("id").on("commerce_customers").on_delete("cascade")
            table.integer("quantity").default(1)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_carts")
