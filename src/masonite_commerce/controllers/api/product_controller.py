from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from ...models.CommerceProduct import CommerceProduct
from masoniteorm.expressions import JoinClause


class ProductController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of products"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        comment_query = JoinClause("commerce_comments as comments").on(
            "comments.product_id", "=", "commerce_products.id"
        )
        meta_query = JoinClause("commerce_metas as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        products = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                CONVERT(metas.price, FLOAT) as price,
                CONVERT(metas.average_rating, FLOAT) as avg_rating,
                metas.stock_status,
                CONVERT(metas.stock_quantity, UNSIGNED) as quantity,
                count(comments.id) as total_comments
            """
            )
            .join(comment_query)
            .join(meta_query)
            .group_by("comments.product_id, metas.id")
            .paginate(per_page, page)
        )

        return {
            "data": products.serialize(),
        }

    def show(self, id: int):
        """Returns a single product"""

        comment_query = JoinClause("commerce_comments as comments").on(
            "comments.product_id", "=", "commerce_products.id"
        )
        meta_query = JoinClause("commerce_metas as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        product = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                CONVERT(metas.price, FLOAT) as price,
                CONVERT(metas.average_rating, FLOAT) as avg_rating,
                metas.stock_status,
                CONVERT(metas.stock_quantity, UNSIGNED) as quantity,
                count(comments.id) as total_comments,
            """
            )
            .join(comment_query)
            .join(meta_query)
            .where("commerce_products.id", "=", id)
            .group_by("comments.product_id, metas.id")
            .first()
        )

        return {
            "data": product.serialize(),
        }
