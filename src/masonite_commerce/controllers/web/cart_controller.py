from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from masonite.configuration import config
from src.masonite_commerce.models.CommerceCart import CommerceCart
from src.masonite_commerce.commerce import Commerce
from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from masoniteorm.expressions import JoinClause


class CartController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = Commerce()

    def index(self, view: View):
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

        return view.render("masonite-commerce:carts/index", {"carts": carts})

    def store(self):
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
            return self.response.back().with_errors("Product out of stock!")

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
                    return self.response.back().with_errors("Cart limit is reached!")

            return self.response.back().with_success("Item added to cart!")

        return self.response.back().with_errors("Product out of stock!")

    def update(self, cart_id):
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
            .where("carts.id", "=", cart_id)
            .first()
        )
        if not product:
            return self.response.back().with_errors("Product out of stock!")

        if product.stock_status == "instock":
            cart = CommerceCart.where(
                {"id": cart_id, "customer_id": customer_id}
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
                    return self.response.back().with_errors("Cart limit is reached!")

            return self.response.back().with_success("Item added to cart!")

        return self.response.back().with_errors("Product out of stock!")

    def destroy(self, cart_id):
        cart = CommerceCart.find(cart_id)
        if not cart:
            return self.response.back().with_errors("Cart not found!")

        cart.delete()

        return self.response.back().with_success("Cart deleted!")