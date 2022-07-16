from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.models.CommerceComment import CommerceComment
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

        comment_query = JoinClause("commerce_comments as comments", clause="left").on(
            "comments.product_id", "=", "commerce_products.id"
        )
        meta_query = JoinClause("commerce_product_meta as metas", clause="left").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        products = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                cast(coalesce(metas.price, 0) as int) as price,
                cast(coalesce(metas.average_rating, 0) as int) as avg_rating,
                metas.stock_status,
                cast(coalesce(metas.stock_quantity, 0) as int) as quantity,
                count(comments.id) as total_comments
            """
            )
            .join(comment_query)
            .join(meta_query)
            .where("commerce_products.status", "=", "published")
            .where("metas.stock_status", "=", "instock")
            .group_by("metas.id, commerce_products.id")
            .paginate(per_page, page)
        )

        return products

    def show(self, id: int):
        """Returns a single product"""

        comment_query = JoinClause("commerce_comments as comments", clause="left").on(
            "comments.product_id", "=", "commerce_products.id"
        )
        meta_query = JoinClause("commerce_product_meta as metas", clause="left").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        product = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                cast(coalesce(metas.price, 0) as int) as price,
                cast(coalesce(metas.average_rating, 0) as int) as avg_rating,
                metas.stock_status,
                cast(coalesce(metas.stock_quantity, 0) as int) as quantity,
                count(comments.id) as total_comments
            """
            )
            .join(comment_query)
            .join(meta_query)
            .where("commerce_products.id", "=", id)
            .with_("meta", "categories", "attributes", "tags")
            .group_by("comments.product_id, metas.id, commerce_products.id")
            .first()
        )

        return {
            "data": product.serialize(),
        }

    def comments(self, id: int):
        """Returns a list of comments for a product"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        comments = CommerceComment.where("product_id", "=", id).paginate(per_page, page)

        return comments
