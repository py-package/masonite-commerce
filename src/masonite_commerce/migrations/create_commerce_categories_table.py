# flake8: noqa: E501
"""CreateCommerceCategoriesTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommerceCategoriesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("commerce_categories") as table:
            table.increments("id")
            table.integer("parent_id").unsigned().nullable()
            table.foreign("parent_id").references("id").on("commerce_categories")
            table.string("title")
            table.string("slug")
            table.string("status")  # draft, published, archived
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_categories")
