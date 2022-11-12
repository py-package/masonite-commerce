from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from ...commerce import Commerce


class CategoryController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = Commerce()

    def index(self, view: View):
        return view.render(
            "masonite-commerce:dashboard/categories/index"
        )