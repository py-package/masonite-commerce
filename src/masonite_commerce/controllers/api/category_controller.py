from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.enums.http_status import HttpStatus
from src.masonite_commerce.models.CommerceCategory import CommerceCategory
from src.masonite_commerce.queries.category_query import CategoryQuery
from src.masonite_commerce.validators.category_rule import CategoryRule


class CategoryController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of categories"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        return (
            CategoryQuery()
            .include("children")
            .null("parent_id")
            .desc("id")
            .paginate(per_page, page)
        )
        return CommerceCategory.with_("children").where_null("parent_id").paginate(per_page, page)

    def store(self):
        """Creates a new category"""
        errors = self.request.validate(CategoryRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE,
            )

        try:
            data = self.request.only("parent_id", "title", "slug", "status")

            data.update({"creator_id": 1})

            category = CommerceCategory.create(data)

            return self.response.json(
                {
                    "category": category.serialize(),
                    "message": "Category created successfully",
                },
                status=HttpStatus.CREATED,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to create category",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE,
            )

    def update(self, id):
        """Updates a category"""

        errors = self.request.validate(CategoryRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE,
            )

        try:
            data = self.request.only("parent_id", "title", "slug", "status")
            category = CommerceCategory.find(id)
            if not category:
                return self.response.json(
                    {
                        "message": "Unable to find category",
                    },
                    status=HttpStatus.NOT_FOUND,
                )

            category.update(data)
            return self.response.json(
                {
                    "message": "Category updated successfully",
                },
                status=HttpStatus.UPDATED,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to update category",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE,
            )

    def destroy(self, id):
        """Deletes a category"""
        CommerceCategory.where("id", "=", id).delete()

        return self.response.json(
            {
                "message": "Category deleted successfully",
            },
            status=HttpStatus.DELETED,
        )
