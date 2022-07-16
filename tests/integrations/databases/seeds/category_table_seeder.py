"""CategoryTableSeeder Seeder."""
from masoniteorm.seeds import Seeder

from config.factories import Factory
from src.masonite_commerce.models.CommerceCategory import CommerceCategory


class CategoryTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceCategory, 50).create()
