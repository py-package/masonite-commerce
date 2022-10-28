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
            table.integer("creator_id").unsigned().nullable()
            table.foreign("creator_id").references("id").on("users").on_delete("set null")
            table.integer("parent_id").unsigned().nullable()
            table.foreign("parent_id").references("id").on("commerce_categories").on_delete("set null")
            table.string("title")
            table.string("slug")
            table.string("status", 12).default("draft")  # draft, published, archived
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("commerce_categories")
