from masonite.tests import TestCase


class TestProductsAPI(TestCase):

    def test_route_exists(self):
        self.assertTrue(self.get('/api/v1/products'))
        self.assertTrue(self.get('/api/v1/products/1'))
        self.assertTrue(self.get('/api/v1/products/1/comments'))
