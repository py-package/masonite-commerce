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
from src.masonite_commerce.models.CommerceAttribute import CommerceAttribute
from src.masonite_commerce.validators.attribute_rule import AttributeRule


class AttributeController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of attributes"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        return CommerceAttribute.paginate(per_page, page)

    def store(self):
        """Creates a new attribute"""

        errors = self.request.validate(AttributeRule)

        if errors:
            return self.response.json({
                "message": "Data validation failed",
                "errors": errors.all()
            }, status=STATUS_UNPROCESSABLE)

        try:
            data = self.request.only("title", "status")
            attribute = CommerceAttribute.create(data)

            return self.response.json({
                "attribute": attribute.serialize(),
                "message": "Attribute created successfully"
            }, status=STATUS_CREATED)
        except:
            return self.response.json({
                "message": "Unable to create attribute",
            }, status=STATUS_UNPROCESSABLE)

    def update(self, id):
        """Updates a attribute"""

        errors = self.request.validate(AttributeRule)

        if errors:
            return self.response.json({
                "message": "Data validation failed",
                "errors": errors.all()
            }, status=STATUS_UNPROCESSABLE)

        try:
            data = self.request.only("title", "status")
            attribute = CommerceAttribute.find(id)
            if not attribute:
                return self.response.json({
                    "message": "Unable to find attribute",
                }, status=STATUS_NOT_FOUND)

            attribute.update(data)
            return self.response.json(
                {"message": "Attribute updated successfully"}, status=STATUS_UPDATED
            )
        except:
            return self.response.json({
                "message": "Unable to update attribute",
            }, status=STATUS_UNPROCESSABLE)

    def destroy(self, id):
        """Deletes a attribute"""
        CommerceAttribute.where("id", "=", id).delete()

        return self.response.json(
            {"message": "Attribute deleted successfully"}, status=STATUS_DELETED
        )
