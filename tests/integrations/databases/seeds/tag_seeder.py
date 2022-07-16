"""TagTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from config.factories import Factory
from src.masonite_commerce.models.CommerceTag import CommerceTag

class TagTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceTag, 10).create()
        