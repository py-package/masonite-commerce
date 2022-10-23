from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.constants.http_status_codes import (
    STATUS_CREATED,
    STATUS_DELETED,
    STATUS_UPDATED,
)
from ...models.CommerceTag import CommerceTag


class TagController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of tags"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))
        return CommerceTag.paginate(per_page, page)

    def show(self, id):
        """Returns a single tag"""

        return CommerceTag.find(id)

    def store(self):
        """Creates a new tag"""

        tag = CommerceTag.create(self.request.all())
        return self.response.json(
            {"tag": tag.serialize(), "message": "Tag created successfully"},
            status=STATUS_CREATED,
        )

    def update(self, id):
        """Updates a tag"""

        tag = CommerceTag.find(id)
        tag.update(self.request.all())
        return self.response.json({"message": "Tag updated successfully"}, status=STATUS_UPDATED)

    def destroy(self, id):
        """Deletes a tag"""
        
        tag = CommerceTag.find(id)
        tag.delete()
        return self.response.json({"message": "Tag deleted successfully"}, status=STATUS_DELETED)
