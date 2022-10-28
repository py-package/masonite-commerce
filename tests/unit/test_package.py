from masonite.tests import TestCase


class TestMasoniteCommerce(TestCase):

    def test_home(self):
        self.get("/").assertOk()
