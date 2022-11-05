from masonite.validation import RuleEnclosure, required, file, is_list

class ProductRule(RuleEnclosure):

    def rules(self):
        """ ... """
        return [
            required([
                'title', 'slug', 'comment_status', 'status',
                "price", "stock_quantity",
            ], messages={
                "title": "Product title is required",
                "slug": "Product slug is required",
                "comment_status": "Product comment status is required",
                "status": "Product status is required",
                "price": "Price is required",
                "stock_quantity": "Stock quantity is required",
            }),
            is_list(["tags", "categories"], messages={
                "tags": "Tags must be a list",
                "categories": "Categories must be a list"
            })

            # file("cover_image", messages="Cover image is required")
        ]