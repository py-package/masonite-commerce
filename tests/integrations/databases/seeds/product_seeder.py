# flake8: noqa F501
"""ProductTableSeeder Seeder."""
import random
from faker import Faker
from masoniteorm.seeds import Seeder

from config.factories import Factory
from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from masoniteorm.query import QueryBuilder


class ProductTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceProduct, 200).create()
        category_builder = QueryBuilder().table("commerce_category_product")
        meta_builder = QueryBuilder().table("commerce_metas")
        tag_builder = QueryBuilder().table("commerce_product_tag")
        attribute_builder = QueryBuilder().table("commerce_product_attribute")

        categories = []
        metas = []
        tags = []
        attributes = []

        fake = Faker()

        for i in range(1, 200):
            random_categories = random.sample(range(1, 50), random.randint(1, 5))
            random_tags = random.sample(range(1, 50), random.randint(1, 5))
            random_attributes = random.sample(range(1, 50), random.randint(1, 5))

            metas.append({
                "product_id": i,
                "price": random.randint(200, 800),
                "sku": random.randint(100, 1000),
                "downloadable": random.choice([True, False]),
                "min_price": random.randint(100, 200),
                "max_price": random.randint(800, 1000),
                "on_sale": random.choice([True, False]),
                "stock_quantity": random.randint(0, 100),
                "stock_status": random.choice(["instock", "outofstock"]),
                "rating_count": random.randint(1, 1000),
                "average_rating": random.randint(1, 5),
                "total_sales": random.randint(1, 1000),
            })
            
            for category in random_categories:
                categories.append({"product_id": i, "category_id": category})

            for tag in random_tags:
                tags.append({"product_id": i, "tag_id": tag})

            for attribute in random_attributes:
                attributes.append({"product_id": i, "attribute_id": attribute, "value": fake.word()})

        category_builder.bulk_create(categories)
        meta_builder.bulk_create(metas)
        tag_builder.bulk_create(tags)
        attribute_builder.bulk_create(attributes)
