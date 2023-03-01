from typing import Optional


class BaseQuery:
    def __init__(self) -> None:
        from wsgi import application

        self.app = application
        self.request = self.app.make("request")

        self.per_page = int(self.request.input("per-page", 10))
        self.page = int(self.request.input("page", 1))

        self.query = None

    def select_raw(self, raw):
        return self.query.select_raw(raw)

    def include(self, *relationships):
        self.query.with_(*relationships)
        return self

    def null(self, column: str):
        """Filters a column to be null"""

        self.query.where_null(column)
        return self

    def not_null(self, column: str):
        """Filters a column to be not null"""

        self.query.where_not_null(column)
        return self

    def desc(self, column: str):
        """Returns the latest model"""

        self.query.order_by(column, "desc")
        return self

    def asc(self, column: str):
        """Returns the oldest model"""

        self.query.order_by(column, "asc")
        return self

    def get(self):
        """Returns a list of models"""

        return self.query.get()
    
    def with_count(self, *relationships):
        """Returns a list of models with counts"""

        self.query.with_count(*relationships)
        return self
    
    def where_not_id(self, id: int):
        """Filters a model by id"""

        self.query.where("id", "!=", id)
        return self

    def paginate(self, per_page: Optional[int] = None, page: Optional[int] = None):
        """Returns a paginated list of models"""

        if not per_page:
            per_page = self.per_page

        if not page:
            page = self.page

        return self.query.paginate(per_page, page)
