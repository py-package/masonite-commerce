"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash
from config.factories import Factory
from tests.integrations.app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "Joe",
                "email": "user@example.com",
                "password": Hash.make("secret"),
                "phone": "+123456789",
            }
        )

        Factory(User, 10).create()
