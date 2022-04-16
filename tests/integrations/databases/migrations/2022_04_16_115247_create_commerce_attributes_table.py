"""CreateCommerceAttributesTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceAttributesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_attributes") as table:
            table.increments("id")
            table.string("title")
            table.string("status", 12).default("published")  # draft, published
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_attributes")
