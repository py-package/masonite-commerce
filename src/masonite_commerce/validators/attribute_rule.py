from masonite.validation import RuleEnclosure, required


class AttributeRule(RuleEnclosure):
    def rules(self):
        """..."""
        return [
            required(
                ["title"],
                messages={
                    "title": "Attribute title is required.",
                },
            )
        ]
