"""CreateCommerceProductsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceProductsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_products") as table:
            table.big_increments("id")
            table.big_integer("creator_id").unsigned().nullable()
            table.foreign("creator_id").references("id").on("users").on_delete("set null")
            table.string("title")
            table.string("slug").unique()
            table.text("excerpt").nullable()
            table.text("content").nullable()
            table.string("cover_image").nullable()
            table.big_integer("comment_count").default(0)
            table.string("comment_status").default("open")  # open, closed
            table.string("status", 20).default("draft")  # draft, published, archived
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_products")
