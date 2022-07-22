"""AttributeTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from config.factories import Factory
from src.masonite_commerce.models.CommerceAttribute import CommerceAttribute


class AttributeTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceAttribute, 50).create()
