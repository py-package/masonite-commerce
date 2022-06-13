"""CommentTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash
from config.factories import Factory
from src.masonite_commerce.models.CommerceComment import CommerceComment

class CommentTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(CommerceComment, 500).create()