from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.enums.http_status import HttpStatus
from src.masonite_commerce.models.CommerceComment import CommerceComment


class CommentController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of categories"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))
        product_id = int(self.request.input("product-id", 0))

        if product_id == 0:
            return CommerceComment.paginate(per_page, page)
        return CommerceComment.where("product_id", "=", product_id).paginate(per_page, page)

    def store(self):
        """Creates a new comment"""

        data = self.request.only("product_id", "star", "comment")
        data.update({"creator_id": self.request.user().id, "status": "pending"})
        comment = CommerceComment.create(data)

        return self.response.json(
            {
                "comment": comment.serialize(),
                "message": "Comment added successfully",
            },
            status=HttpStatus.CREATED,
        )

    def destroy(self, id):
        """Deletes a comment"""
        comment = CommerceComment.find(id)
        comment.delete()

        return self.response.json(
            {
                "message": "Comment deleted successfully",
            },
            status=HttpStatus.DELETED,
        )
