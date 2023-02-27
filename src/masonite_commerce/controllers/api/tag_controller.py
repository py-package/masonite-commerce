from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.enums.http_status import HttpStatus
from src.masonite_commerce.models.CommerceTag import CommerceTag
from src.masonite_commerce.queries.tag_query import TagQuery
from src.masonite_commerce.validators.tag_rule import TagRule


class TagController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of tags"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        query = (
            TagQuery()
            .with_count("products")
            .asc("title")
        )

        if self.request.input("title", None):
            query.where_title(self.request.input("title", None))

        return query.paginate(per_page, page)

    def store(self):
        """Creates a new tag"""

        errors = self.request.validate(TagRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

        try:
            data = self.request.only("title", "slug")
            tag = CommerceTag.create(data)

            return self.response.json(
                {
                    "tag": tag.serialize(),
                    "message": "Tag created successfully",
                },
                status=HttpStatus.CREATED.value,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to create tag",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

    def update(self, id):
        """Updates a tag"""

        errors = self.request.validate(TagRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

        try:
            data = self.request.only("title", "slug")
            tag = CommerceTag.find(id)
            if not tag:
                return self.response.json(
                    {
                        "message": "Unable to find tag",
                    },
                    status=HttpStatus.NOT_FOUND.value,
                )

            tag.update(data)
            return self.response.json(
                {
                    "message": "Tag updated successfully",
                },
                status=HttpStatus.UPDATED.value,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to update tag",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

    def destroy(self, id):
        """Deletes a tag"""

        CommerceTag.where("id", "=", id).delete()

        return self.response.json(
            {
                "message": "Tag deleted successfully",
            },
            status=HttpStatus.DELETED.value,
        )
