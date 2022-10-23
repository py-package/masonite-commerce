from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.constants.http_status_codes import (
    STATUS_CREATED,
    STATUS_DELETED,
    STATUS_UPDATED,
)
from ...models.CommerceAttribute import CommerceAttribute


class AttributeController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of attributes"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        return CommerceAttribute.paginate(per_page, page)

    def show(self, id):
        """Returns a single attribute"""

        return CommerceAttribute.find(id)

    def store(self):
        """Creates a new attribute"""

        attribute = CommerceAttribute.create(self.request.all())

        return self.response.json(
            {"attribute": attribute.serialize(), "message": "Category created successfully"},
            status=STATUS_CREATED,
        )

    def update(self, id):
        """Updates a attribute"""

        attribute = CommerceAttribute.find(id)
        attribute.update(self.request.all())

        return self.response.json(
            {"message": "Attribute updated successfully"}, status=STATUS_UPDATED
        )

    def destroy(self, id):
        """Deletes a attribute"""
        attribute = CommerceAttribute.find(id)
        attribute.delete()

        return self.response.json(
            {"message": "Attribute deleted successfully"}, status=STATUS_DELETED
        )
