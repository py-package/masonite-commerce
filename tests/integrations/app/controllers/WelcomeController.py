"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def commerce(self, view: View):
        # comment_query = JoinClause("commerce_comments as comments", clause="left").on(
        #     "comments.product_id", "=", "commerce_products.id"
        # )
        # meta_query = JoinClause("commerce_metas as metas", clause="left").on(
        #     "metas.product_id", "=", "commerce_products.id"
        # )

        # products = (
        #     ProductQuery().select_raw(
        #         """
        #         commerce_products.*,
        #         cast(coalesce(metas.price, 0) as int) as price,
        #         cast(coalesce(metas.average_rating, 0) as int) as avg_rating,
        #         metas.stock_status,
        #         cast(coalesce(metas.stock_quantity, 0) as int) as quantity,
        #         count(comments.id) as total_comments
        #     """
        #     )
        #     .join(comment_query)
        #     .join(meta_query)
        #     .where("commerce_products.status", "=", "published")
        #     .where("metas.stock_status", "=", "instock")
        #     .group_by("metas.id, commerce_products.id")
        #     .paginate(8, 1)
        # )
        return view.render("commerce")
