# flake8: noqa: E501
import random

from faker import Faker
from masonite.commands import Command
from masonite.facades import Hash
from masoniteorm.query import QueryBuilder


class CommerceSeed(Command):
    """
    Sets up dummy data for the commerce demo.

    commerce:seed
        {--c|clear : Clears the database}
    """

    def handle(self):
        clear = self.option("clear")
        if clear:
            self.info("Resetting Database")
            self.reset()
        else:
            self.reset()
            self.seed_users()
            self.seed_categories()
            self.seed_products()
            self.seed_metas()
            self.seed_attributes()
            self.seed_comments()

    def reset(self):
        """Reset Database"""

        QueryBuilder().table("users").where_in("email", ["john@doe.com", "jane@doe.com"]).delete()
        QueryBuilder().table("commerce_products").truncate(True)
        QueryBuilder().table("commerce_categories").truncate(True)
        QueryBuilder().table("commerce_metas").truncate(True)
        QueryBuilder().table("commerce_attributes").truncate(True)
        QueryBuilder().table("commerce_product_attribute").truncate(True)
        QueryBuilder().table("commerce_comments").truncate(True)

    def seed_users(self):
        """Seed User Data"""
        self.info("Seeding User Data")
        users = [
            {
                "name": "John Doe",
                "email": "john@doe.com",
                "password": Hash.make("password"),
            },
            {
                "name": "Jane Doe",
                "email": "jane@doe.com",
                "password": Hash.make("password"),
            },
        ]
        QueryBuilder().table("users").bulk_create(users)

    def seed_categories(self):
        """Seed Category Data"""
        self.info("Seeding Category Data")

        fake = Faker()

        user = QueryBuilder().table("users").where("email", "john@doe.com").first()

        categories = []

        for _ in range(50):
            title = fake.unique.word().title()
            slug = title.lower().replace(" ", "-")
            categories.append(
                {
                    "creator_id": user.get("id"),
                    "title": title,
                    "slug": slug,
                    "status": "published",
                }
            )
        QueryBuilder().table("commerce_categories").bulk_create(categories)

    def seed_products(self):
        """Seed Product Data"""
        self.info("Seeding Product Data")
        fake = Faker()
        user = QueryBuilder().table("users").where("email", "john@doe.com").first()
        products = []

        for _ in range(50):
            title = fake.unique.word().title()
            slug = title.lower().replace(" ", "-")
            products.append(
                {
                    "creator_id": user.get("id"),
                    "title": title,
                    "slug": slug,
                    "excerpt": fake.sentence(),
                    "content": fake.text(),
                    "cover_image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
                    "comment_status": "open",
                    "status": "published",
                }
            )

        QueryBuilder().table("commerce_products").bulk_create(products)
        products = QueryBuilder().table("commerce_products").get()
        category_product = []

        for product in products:
            category_product.append(
                {
                    "product_id": product.get("id"),
                    "category_id": random.randint(1, 50),
                }
            )

        QueryBuilder().table("commerce_category_product").bulk_create(category_product)

    def seed_metas(self):
        """Seed Meta Data"""
        self.info("Seeding Meta Data")
        fake = Faker()
        metas = []
        products = QueryBuilder().table("commerce_products").get()

        for product in products:
            min_price = random.randint(1, 100)
            max_price = random.randint(min_price, min_price + 100)
            price = random.randint(min_price, max_price)

            metas.append(
                {
                    "product_id": product.get("id"),
                    "sku": f"SKU-{fake.unique.word().upper().replace(' ', '-')}",
                    "virtual": random.choice([True, False]),
                    "downloadable": random.choice([True, False]),
                    "price": price,
                    "min_price": min_price,
                    "max_price": max_price,
                    "on_sale": random.choice([True, False]),
                    "stock_quantity": random.randint(1, 100),
                    "stock_status": random.choice(["instock", "outofstock", "onbackorder"]),
                    "rating_count": random.randint(1, 5),
                    "average_rating": random.randint(1, 5),
                    "total_sales": random.randint(1, 100),
                    "tax_status": random.choice(["taxable", "shipping", "none"]),
                }
            )

        QueryBuilder().table("commerce_metas").bulk_create(metas)

    def seed_attributes(self):
        """Seed Attribute Data"""
        self.info("Seeding Attribute Data")
        products = QueryBuilder().table("commerce_products").get()

        attributes = [
            {
                "title": "Color",
            },
            {
                "title": "Size",
            },
            {
                "title": "Weight",
            },
        ]

        QueryBuilder().table("commerce_attributes").bulk_create(attributes)

        attribute_product = []

        for product in products:
            attribute_product.append(
                {
                    "product_id": product.get("id"),
                    "attribute_id": 2,
                    "value": random.choice(["Red", "Blue", "Green"]),
                }
            )

            if random.choice([True, False]):
                attribute_product.append(
                    {
                        "product_id": product.get("id"),
                        "attribute_id": 2,
                        "value": random.choice(["Small", "Medium", "Large"]),
                    }
                )

            if random.choice([True, False]):
                attribute_product.append(
                    {
                        "product_id": product.get("id"),
                        "attribute_id": 3,
                        "value": random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                    }
                )

        QueryBuilder().table("commerce_product_attribute").bulk_create(attribute_product)

    def seed_comments(self):
        """Seed Comment Data"""
        self.info("Seeding Comment Data")
        fake = Faker()
        user = QueryBuilder().table("users").where("email", "john@doe.com").first()
        products = QueryBuilder().table("commerce_products").get()
        comments = []

        for product in products:
            for _ in range(random.randint(1, 10)):
                comments.append(
                    {
                        "creator_id": user.get("id"),
                        "product_id": product.get("id"),
                        "content": fake.sentence(),
                        "status": random.choice(["approved", "pending", "spam"]),
                    }
                )

        QueryBuilder().table("commerce_comments").bulk_create(comments)
