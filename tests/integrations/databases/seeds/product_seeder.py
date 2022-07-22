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
        category_builder = QueryBuilder().table("commerce_category_product")
        meta_builder = QueryBuilder().table("commerce_product_meta")
        tag_builder = QueryBuilder().table("commerce_product_tag")

        categories = []
        metas = []
        tags = []

        for i in range(1, 200):
            num = random.randint(2, 5)
            random_categories = random.sample(range(1, 50), num)
            random_tags = random.sample(range(1, 50), num)

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


        category_builder.bulk_create(categories)
        meta_builder.bulk_create(metas)
        tag_builder.bulk_create(tags)
