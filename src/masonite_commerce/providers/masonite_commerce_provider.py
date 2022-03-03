"""A MasoniteCommerceProvider Service Provider."""

from masonite.packages import PackageProvider


class MasoniteCommerceProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_commerce")
            .name("masonite-commerce")
            .config("config/masonite_commerce.py", publish=True)
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
