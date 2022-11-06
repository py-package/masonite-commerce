"""CreateCommerceProductVariationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceProductVariationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_product_variations") as table:
            table.increments("id")
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete(
                "cascade"
            )
            table.string("sku", 100).nullable()
            table.decimal("price", 19, 4).nullable()
            table.decimal("min_price", 19, 4).nullable()
            table.decimal("max_price", 19, 4).nullable()
            table.boolean("on_sale").default(False)
            table.double("stock_quantity").nullable()
            table.string("stock_status", 100).default("instock")
            table.integer("total_sales").default(0)
            table.string("image").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_product_variations")
