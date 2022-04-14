from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from ...commerce import Commerce
from masoniteorm.query import QueryBuilder
from ...models.CommerceProduct import CommerceProduct
from ...models.CommerceCategory import CommerceCategory


class CommerceController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = Commerce()

    def index(self, view: View):
        QueryBuilder().table("users").select("id", "name", "email").all().serialize()
        CommerceProduct.with_("categories", "meta").all()
        CommerceCategory.with_("products").all()
        return view.render("masonite-commerce:index", {})
