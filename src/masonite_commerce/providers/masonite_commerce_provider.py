"""A MasoniteCommerceProvider Service Provider."""

from masonite.packages import PackageProvider

from ..commands import CommerceSeed


class MasoniteCommerceProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_commerce")
            .name("masonite-commerce")
            .config("config/commerce.py", publish=True)
            .routes("routes/web.py", "routes/api.py")
            .migrations(
                "migrations/create_commerce_products_table.py",
                "migrations/create_commerce_categories_table.py",
                "migrations/create_commerce_metas_table.py",
                "migrations/create_commerce_attributes_table.py",
                "migrations/create_commerce_category_product_table.py",
                "migrations/create_commerce_product_attribute_table.py",
                "migrations/create_commerce_comments_table.py",
            )
            .views("templates", publish=False)
        )

    def register(self):
        super().register()
        self.application.make("commands").add(CommerceSeed())

    def boot(self):
        """Boots services required by the container."""
        pass
