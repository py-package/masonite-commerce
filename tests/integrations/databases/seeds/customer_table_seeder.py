"""CustomerTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from config.factories import Factory
from src.masonite_commerce.models.CommerceCustomer import CommerceCustomer


class CustomerTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceCustomer, 10).create()
