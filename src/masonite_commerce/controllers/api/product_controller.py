from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from ...models.CommerceProduct import CommerceProduct


class ProductController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """ Returns a list of products """
        
        return CommerceProduct.paginate(10)
