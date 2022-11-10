from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.enums.http_status import HttpStatus
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
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE,
            )

        try:
            data = self.request.only("title", "status")
            attribute = CommerceAttribute.create(data)

            return self.response.json(
                {
                    "attribute": attribute.serialize(),
                    "message": "Attribute created successfully",
                },
                status=HttpStatus.CREATED,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to create attribute",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE,
            )

    def update(self, id):
        """Updates a attribute"""

        errors = self.request.validate(AttributeRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE,
            )

        try:
            data = self.request.only("title", "status")
            attribute = CommerceAttribute.find(id)
            if not attribute:
                return self.response.json(
                    {
                        "message": "Unable to find attribute",
                    },
                    status=HttpStatus.NOT_FOUND,
                )

            attribute.update(data)
            return self.response.json(
                {
                    "message": "Attribute updated successfully",
                },
                status=HttpStatus.UPDATED,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to update attribute",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE,
            )

    def destroy(self, id):
        """Deletes a attribute"""
        CommerceAttribute.where("id", "=", id).delete()

        return self.response.json(
            {
                "message": "Attribute deleted successfully",
            },
            status=HttpStatus.DELETED,
        )
