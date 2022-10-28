from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.constants.http_status_codes import (
    STATUS_CREATED,
    STATUS_DELETED,
    STATUS_NOT_FOUND,
    STATUS_UNPROCESSABLE,
    STATUS_UPDATED,
)
from src.masonite_commerce.models.CommerceTag import CommerceTag
from src.masonite_commerce.validators.tag_rule import TagRule


class TagController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of tags"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))
        return CommerceTag.paginate(per_page, page)

    def store(self):
        """Creates a new tag"""

        errors = self.request.validate(TagRule)

        if errors:
            return self.response.json({
                "message": "Data validation failed",
                "errors": errors.all()
            }, status=STATUS_UNPROCESSABLE)

        try:
            data = self.request.only("title", "slug")
            tag = CommerceTag.create(data)

            return self.response.json({
                "tag": tag.serialize(),
                "message": "Tag created successfully"
            }, status=STATUS_CREATED)
        except:
            return self.response.json({
                "message": "Unable to create tag",
            }, status=STATUS_UNPROCESSABLE)

    def update(self, id):
        """Updates a tag"""

        errors = self.request.validate(TagRule)

        if errors:
            return self.response.json({
                "message": "Data validation failed",
                "errors": errors.all()
            }, status=STATUS_UNPROCESSABLE)

        try:
            data = self.request.only("title", "slug")
            tag = CommerceTag.find(id)
            if not tag:
                return self.response.json({
                    "message": "Unable to find tag",
                }, status=STATUS_NOT_FOUND)

            tag.update(data)
            return self.response.json(
                {"message": "Tag updated successfully"}, status=STATUS_UPDATED
            )
        except:
            return self.response.json({
                "message": "Unable to update tag",
            }, status=STATUS_UNPROCESSABLE)

    def destroy(self, id):
        """Deletes a tag"""
        
        CommerceTag.where("id", "=", id).delete()

        return self.response.json(
            {"message": "Tag deleted successfully"}, status=STATUS_DELETED
        )
