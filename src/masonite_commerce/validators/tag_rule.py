from masonite.validation import RuleEnclosure, required


class TagRule(RuleEnclosure):
    def rules(self):
        """..."""
        return [
            required(
                ["title", "slug"],
                messages={"title": "Tag title is required.", "slug": "Tag slug is required."},
            )
        ]
