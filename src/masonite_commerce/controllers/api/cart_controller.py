from masonite.configuration import config
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masoniteorm.expressions import JoinClause

from src.masonite_commerce.enums.http_status import HttpStatus
from src.masonite_commerce.models.CommerceCart import CommerceCart
from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from src.masonite_commerce.validators.cart_rule import CartRule


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

        carts = CommerceCart.with_(
            {
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
            },
            "customer",
        ).paginate(per_page, page)

        return carts

    def store(self):
        """Creates a new cart"""

        errors = self.request.validate(CartRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

        try:
            customer_id = 1

            data = self.request.only("product_id", "quantity")

            data.update({"customer_id": customer_id, "quantity": int(data.get("quantity", 1))})

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
                .where("commerce_products.id", "=", data.get("product_id"))
                .first()
            )
            if not product:
                return self.response.json(
                    {
                        "message": "Product out of stock!",
                    },
                    status=HttpStatus.UNPROCESSABLE.value,
                )

            if product.stock_status == "instock":
                cart = CommerceCart.where(
                    {"product_id": data.get("product_id"), "customer_id": customer_id}
                ).first()
                if not cart:
                    cart = CommerceCart.create(
                        {
                            "product_id": product.id,
                            "customer_id": customer_id,
                            "quantity": data.get("quantity"),
                        }
                    )
                else:
                    cart_limit = config("commerce.cart_limit", 0)
                    if cart_limit == 0 or cart_limit > cart.quantity:
                        cart.update({"quantity": cart.quantity + data.get("quantity")})
                    else:
                        return self.response.json(
                            {
                                "message": "Cart limit is reached!",
                            },
                            status=HttpStatus.UNPROCESSABLE.value,
                        )

                return self.response.json(
                    {"message": "Item added to cart!"}, status=HttpStatus.CREATED.value
                )

            return self.response.json(
                {
                    "message": "Product out of stock!",
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to create cart",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

    def update(self, id):
        """Updates a cart"""

        errors = self.request.validate(CartRule)

        if errors:
            return self.response.json(
                {
                    "message": "Data validation failed",
                    "errors": errors.all(),
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

        try:
            customer_id = 1

            data = self.request.only("product_id", "quantity")

            data.update({"customer_id": customer_id, "quantity": int(data.get("quantity", 1))})

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
                return self.response.json(
                    {
                        "message": "Product out of stock",
                    },
                    status=HttpStatus.UNPROCESSABLE.value,
                )

            cart = CommerceCart.where({"id": id, "customer_id": customer_id}).first()

            if int(data.get("quantity")) < 1:
                cart.delete()
                return self.response.json(
                    {
                        "message": "Cart deleted successfully",
                    },
                    status=HttpStatus.DELETED.value,
                )

            if product.stock_status == "instock":
                cart_limit = config("commerce.cart_limit", 0)
                if not cart:
                    if cart_limit > data.get("quantity"):
                        return self.response.json(
                            {
                                "message": "Cart limit is reached",
                            },
                            status=HttpStatus.UNPROCESSABLE.value,
                        )
                    else:
                        CommerceCart.create(data)
                else:
                    if cart_limit == 0 or cart_limit >= data.get("quantity"):
                        cart.update({"quantity": data.get("quantity")})
                    else:
                        return self.response.json(
                            {
                                "message": "Cart limit is reached",
                            },
                            status=HttpStatus.UNPROCESSABLE.value,
                        )

                return self.response.json(
                    {
                        "message": "Cart updated",
                    },
                    status=HttpStatus.UPDATED.value,
                )

            return self.response.json(
                {
                    "message": "Product out of stock",
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )
        except Exception as e:
            return self.response.json(
                {
                    "message": "Unable to update cart",
                    "error": e.message,
                },
                status=HttpStatus.UNPROCESSABLE.value,
            )

    def destroy(self, id):
        CommerceCart.where("id", "=", id).delete()
        return self.response.json(
            {
                "message": "Cart deleted!",
            },
            status=HttpStatus.DELETED.value,
        )
