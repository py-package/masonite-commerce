"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder
from tests.integrations.databases.seeds.attribute_seeder import AttributeTableSeeder
from tests.integrations.databases.seeds.category_table_seeder import CategoryTableSeeder
from tests.integrations.databases.seeds.comment_table_seeder import CommentTableSeeder
from tests.integrations.databases.seeds.product_seeder import ProductTableSeeder
from tests.integrations.databases.seeds.tag_seeder import TagTableSeeder

from .user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(CategoryTableSeeder)
        self.call(TagTableSeeder)
        self.call(AttributeTableSeeder)
        self.call(ProductTableSeeder)
        self.call(CommentTableSeeder)
