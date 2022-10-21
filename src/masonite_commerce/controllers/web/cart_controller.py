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
        carts = CommerceCart.with_("product", "customer").all()
        return carts
        return view.render("masonite-commerce:index", {})

    def add_to_cart(self):
        product_id = self.request.input("product_id")
        quantity = int(self.request.input("quantity", 1))
        customer_id = 1

        meta_query = JoinClause("commerce_product_meta as metas").on(
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
            print("Product out of stock!")
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
                    print("Cart limit is reached!")
                    return self.response.back().with_errors("Cart limit is reached!")

            print("Item added to cart!")
            return self.response.back().with_success("Item added to cart!")

        print("Product out of stock!")
        return self.response.back().with_errors("Product out of stock!")
