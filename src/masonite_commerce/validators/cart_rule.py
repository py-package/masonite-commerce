from masonite.validation import RuleEnclosure, required

class CartRule(RuleEnclosure):

    def rules(self):
        """ ... """
        return [
            required(['product_id', 'quantity'], messages={
                "product_id": "Product ID is required.",
                "quantity": "Quantity is required."
            })
        ]