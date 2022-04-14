from masonite.commands import Command
from masoniteorm.query import QueryBuilder
from masonite.facades import Hash

class CommerceSeed(Command):
    """
    Sets up dummy data for the commerce demo.

    commerce:seed
        {--c|clear : Clears the database}
    """

    def handle(self):
        clear = self.option('clear')
        if clear:
            self.info("Resetting Database")
            self.reset()
        else:
            self.reset()
            self.seed_users()
            self.seed_categories()
            self.seed_products()


    def reset(self):
        """Reset Database
        """
    
        QueryBuilder().table('users').where_in("email", ["john@doe.com", "jane@doe.com"]).delete()
        QueryBuilder().table('commerce_products').truncate(True)
        QueryBuilder().table('commerce_categories').truncate(True)
        QueryBuilder().table('commerce_metas').truncate(True)

    def seed_users(self):
        """Seed User Data
        """
        self.info("Seeding User Data")
        users = [
            {
                "name": "John Doe",
                "email": "john@doe.com",
                "password": Hash.make("password"),
            }, {
                "name": "Jane Doe",
                "email": "jane@doe.com",
                "password": Hash.make("password"),
            }
        ]
        QueryBuilder().table('users').bulk_create(users)

    def seed_categories(self):
        """Seed Category Data
        """
        self.info("Seeding Category Data")
        user = QueryBuilder().table('users').where("email", "john@doe.com").first()
        categories = [
            {
                "creator_id": user.get("id"),
                "title": "Electronics",
                "slug": "electronics",
                "status": "published",
            }, {
                "creator_id": user.get("id"),
                "title": "Furniture",
                "slug": "furniture",
                "status": "published",
            }, {
                "creator_id": user.get("id"),
                "title": "Clothing",
                "slug": "clothing",
                "status": "published",
            }
        ]
        QueryBuilder().table('commerce_categories').bulk_create(categories)

    def seed_products(self):
        """Seed Product Data
        """
        self.info("Seeding Product Data")
        user = QueryBuilder().table('users').where("email", "john@doe.com").first()
        products = [
            {
                "creator_id": user.get("id"),
                "title": "iPhone X",
                "slug": "iphone-x",
                "excerpt": "The iPhone X is a line of smartphones designed and marketed by Apple Inc. It is the successor to the iPhone 7 series, the most popular model in the smartphone market.",
                "content": "The iPhone X is a line of smartphones designed and marketed by Apple Inc. It is the successor to the iPhone 7 series, the most popular model in the smartphone market.",
                "cover_image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
                "comment_count": 0,
                "comment_status": "open",
                "status": "published",
            }, {
                "creator_id": user.get("id"),
                "title": "Macbook Pro",
                "slug": "macbook-pro",
                "excerpt": "The MacBook Pro is a line of laptop computers developed and manufactured by Apple Inc. It is the latest generation of the Macintosh portable personal computer.",
                "content": "The MacBook Pro is a line of laptop computers developed and manufactured by Apple Inc. It is the latest generation of the Macintosh portable personal computer.",
                "cover_image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
                "comment_count": 0,
                "comment_status": "open",
                "status": "published",
            }, {
                "creator_id": user.get("id"),
                "title": "Macbook Air",
                "slug": "macbook-air",
                "excerpt": "The MacBook Air is a line of laptop computers developed and manufactured by Apple Inc. It is the latest generation of the Macintosh portable personal computer.",
                "content": "The MacBook Air is a line of laptop computers developed and manufactured by Apple Inc. It is the latest generation of the Macintosh portable personal computer.",
                "cover_image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
                "comment_count": 0,
                "comment_status": "open",
                "status": "published",
            }
        ]

        QueryBuilder().table('commerce_products').bulk_create(products)
        
        category = QueryBuilder().table('commerce_categories').where("title", "electronics").first()
        products = QueryBuilder().table('commerce_products').get()

        category_product = []

        for product in products:
            category_product.append({
                "product_id": product.get("id"),
                "category_id": category.get("id"),
            })

        QueryBuilder().table('commerce_category_product').bulk_create(category_product)