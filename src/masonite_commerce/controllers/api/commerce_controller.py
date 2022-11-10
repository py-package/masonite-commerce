from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response


class CommerceController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        # is_ajax = self.request.is_ajax()
        return self.response.json(
            {
                "message": "Hello Masonite Commerce!",
            }
        )
