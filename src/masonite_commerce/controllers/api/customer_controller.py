# flake8: noqa F401
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.models.CommerceCustomer import CommerceCustomer


class CustomerController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of products"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        customers = (
            CommerceCustomer.paginate(per_page, page)
        )

        return customers

    def store(self):
        pass

    def update(self, id: int):
        pass

    def show(self, id: int):
        pass
