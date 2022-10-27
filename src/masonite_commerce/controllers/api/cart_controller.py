from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.configuration import config

from src.masonite_commerce.constants.http_status_codes import (
    STATUS_CREATED,
    STATUS_DELETED,
    STATUS_UPDATED,
    STATUS_UNPROCESSABLE
)
from src.masonite_commerce.models.CommerceCart import CommerceCart
from masoniteorm.expressions import JoinClause

from src.masonite_commerce.models.CommerceProduct import CommerceProduct


class CartController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """Returns a list of tags"""

        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        comment_query = JoinClause("commerce_comments as comments").on(
            "comments.product_id", "=", "commerce_products.id"
        )

        meta_query = JoinClause("commerce_metas as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        carts = CommerceCart.with_({
            "product": lambda q: q.select_raw(
                """
                    commerce_products.*,
                    CAST(metas.price AS DECIMAL(10, 2)) AS price,
                    CAST(metas.average_rating AS FLOAT) AS avg_rating,
                    CAST(metas.stock_quantity AS UNSIGNED) AS quantity,
                    metas.stock_status,
                    count(comments.id) as total_comments
                """
            )
            .join(comment_query)
            .join(meta_query)
            .group_by("comments.product_id, metas.id")
        }, "customer").paginate(per_page, page)

        return carts

    def store(self):
        """Creates a new cart"""

        product_id = self.request.input("product_id")
        quantity = int(self.request.input("quantity", 1))
        customer_id = 1

        meta_query = JoinClause("commerce_metas as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        product = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                CAST(metas.price AS DECIMAL(10, 2)) AS price,
                CAST(metas.average_rating AS FLOAT) AS avg_rating,
                CAST(metas.stock_quantity AS UNSIGNED) AS quantity,
                metas.stock_status
            """
            )
            .join(meta_query)
            .group_by("metas.id")
            .where("commerce_products.id", "=", product_id)
            .first()
        )
        if not product:
            return self.response.json({
                "message": "Product out of stock!",
            }, status=STATUS_UNPROCESSABLE)

        if product.stock_status == "instock":
            cart = CommerceCart.where(
                {"product_id": product_id, "customer_id": customer_id}
            ).first()
            if not cart:
                cart = CommerceCart.create(
                    {"product_id": product.id, "customer_id": customer_id, "quantity": quantity}
                )
            else:
                cart_limit = config("commerce.cart_limit", 0)
                if cart_limit == 0 or cart_limit > cart.quantity:
                    cart.update({"quantity": cart.quantity + quantity})
                else:
                    return self.response.json({
                        "message": "Cart limit is reached!",
                    }, status=STATUS_UNPROCESSABLE)

            return self.response.json({
                "message": "Item added to cart!"
            }, status=STATUS_CREATED)

        return self.response.json({
            "message": "Product out of stock!",
        }, status=STATUS_UNPROCESSABLE)

    def update(self, id):
        """Updates a cart"""
        quantity = int(self.request.input("quantity", 1))
        customer_id = 1

        meta_query = JoinClause("commerce_metas as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        cart_query = JoinClause("commerce_carts as carts").on(
            "carts.product_id", "=", "commerce_products.id"
        )

        product = (
            CommerceProduct.select_raw(
                """
                commerce_products.*,
                CAST(metas.price AS DECIMAL(10, 2)) AS price,
                CAST(metas.average_rating AS FLOAT) AS avg_rating,
                CAST(metas.stock_quantity AS UNSIGNED) AS quantity,
                metas.stock_status
            """
            )
            .join(meta_query)
            .join(cart_query)
            .group_by("metas.id")
            .where("carts.id", "=", id)
            .first()
        )
        if not product:
            return self.response.json({
                "message": "Product out of stock!",
            }, status=STATUS_UNPROCESSABLE)

        if product.stock_status == "instock":
            cart = CommerceCart.where(
                {"id": id, "customer_id": customer_id}
            ).first()
            if not cart:
                cart = CommerceCart.create(
                    {"product_id": product.id, "customer_id": customer_id, "quantity": quantity}
                )
            else:
                cart_limit = config("commerce.cart_limit", 0)
                if cart_limit == 0 or cart_limit > quantity:
                    cart.update({"quantity": quantity})
                else:
                    return self.response.json({
                        "message": "Cart limit is reached!",
                    }, status=STATUS_UNPROCESSABLE)

            return self.response.json({
                "message": "Cart updated!"
            }, status=STATUS_UPDATED)

        return self.response.json({
            "message": "Product out of stock!",
        }, status=STATUS_UNPROCESSABLE)

    def destroy(self, id):
        cart = CommerceCart.find(id)
        if not cart:
            return self.response.json({
                "message": "Cart not found!"
            })

        cart.delete()

        return self.response.json({
            "message": "Cart deleted!"
        }, status=STATUS_DELETED)
