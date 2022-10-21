from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from ...commerce import Commerce
from ...models.CommerceProduct import CommerceProduct
from masoniteorm.expressions import JoinClause


class CommerceController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = Commerce()

    def index(self, view: View):
        # QueryBuilder().table("users").select("id", "name", "email").all().serialize()
        # CommerceProduct.with_("categories", "meta").all()
        # CommerceCategory.with_("products").all()
        return view.render("masonite-commerce:index", {})

    def products(self, view: View):
        per_page = int(self.request.input("per-page", 10))
        page = int(self.request.input("page", 1))

        comment_query = JoinClause("commerce_comments as comments").on(
            "comments.product_id", "=", "commerce_products.id"
        )
        meta_query = JoinClause("commerce_product_meta as metas").on(
            "metas.product_id", "=", "commerce_products.id"
        )

        products = (
            CommerceProduct.select_raw(
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
            .paginate(per_page, page)
        )

        return view.render(
            "masonite-commerce:products/index",
            {
                "products": products,
            },
        )

    def show(self, view: View):
        comment_query = JoinClause("commerce_comments as comments").on(
            "comments.product_id", "=", "commerce_products.id"
        )
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
                metas.stock_status,
                count(comments.id) as total_comments
            """
            )
            .join(comment_query)
            .join(meta_query)
            .group_by("comments.product_id, metas.id")
            .where("commerce_products.slug", "=", self.request.param("slug"))
            .first()
        )

        return view.render(
            "masonite-commerce:products/show",
            {
                "product": product,
            },
        )
