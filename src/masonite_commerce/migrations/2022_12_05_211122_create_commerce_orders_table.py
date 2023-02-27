# flake8: noqa F501
"""CreateCommerceOrdersTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceOrdersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_orders") as table:
            table.increments("id")
            table.integer("customer_id").unsigned()
            table.foreign("customer_id").references("id").on("commerce_customers").on_delete(
                "cascade"
            )
            table.datetime("order_date")
            table.datetime("shipped_date").nullable()
            table.datetime("delivered_date").nullable()
            table.string("status").default("pending") # pending, shipped, delivered
            table.string("payment_method").default("cash") # cash, credit card, paypal
            table.string("payment_status").default("pending") # pending, paid
            table.string("shipping_method").default("standard") # standard, express
            table.boolean("is_taxable").default(False)
            table.string("notes").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_orders")
