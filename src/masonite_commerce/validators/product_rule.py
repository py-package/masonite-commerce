from masonite.validation import RuleEnclosure, required, is_in, is_list, when

class ProductRule(RuleEnclosure):

    def rules(self):
        """ ... """
        return [
            required([
                'title', 'slug',
                "price", "stock_quantity",
            ], messages={
                "title": "Product title is required",
                "slug": "Product slug is required",
                "comment_status": "Product comment status is required",
                "status": "Product status is required",
                "price": "Price is required",
                "stock_quantity": "Stock quantity is required",
            }),
            is_in("status", ["draft", "published"]),
            is_in("comment_status", ["open", "closed"]),
        ]