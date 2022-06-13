"""ProductTableSeeder Seeder."""
import random
from masoniteorm.seeds import Seeder

from config.factories import Factory
from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from masoniteorm.query import QueryBuilder

class ProductTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceProduct, 200).create()
        builder = QueryBuilder().table("commerce_category_product")
        data = []
        for i in range(1, 200):
            num = random.randint(2, 5)
            items = random.sample(range(1, 50), num)
            
            for item in items:
                data.append({"product_id": i if i != 0 else 1, "category_id": item})
                
        builder.bulk_create(data)