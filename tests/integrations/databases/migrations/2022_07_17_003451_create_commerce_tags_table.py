"""CreateCommerceTagsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceTagsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_tags") as table:
            table.increments("id")
            table.string("title")
            table.string("slug")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_tags")
