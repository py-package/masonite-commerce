from masonite.validation import RuleEnclosure, required


class CategoryRule(RuleEnclosure):
    def rules(self):
        """..."""
        return [
            required(
                ["title", "slug"],
                messages={
                    "title": "Category title is required.",
                    "slug": "Category short name is required.",
                },
            )
        ]
