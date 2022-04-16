"""CreateCommerceCommentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceCommentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_comments") as table:
            table.increments("id")
            table.integer("creator_id").unsigned().nullable()
            table.foreign("creator_id").references("id").on("users").on_delete("set null")
            table.integer("parent_id").unsigned().nullable()
            table.foreign("parent_id").references("id").on("commerce_comments").on_delete(
                "set null"
            )
            table.integer("product_id").unsigned()
            table.foreign("product_id").references("id").on("commerce_products").on_delete(
                "cascade"
            )
            table.text("content")
            table.string("status", 12)  # draft, published, archived
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_comments")
