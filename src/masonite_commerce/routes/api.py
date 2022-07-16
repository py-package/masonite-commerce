from masonite.routes import Route
from masonite.configuration import config

from ..controllers.api.category_controller import CategoryController
from ..controllers.api.product_controller import ProductController
from ..controllers.api.tag_controller import TagController


ROUTES = Route.group(
    [
        # Product Routes
        Route.get("/products", ProductController.index),
        Route.get("/products/@id:int", ProductController.show),
        Route.get("/products/@id:int/comments", ProductController.comments),
        # Category Routes
        Route.get("/categories", CategoryController.index),
        # Tag Routes
        Route.get("/tags", TagController.index),
    ],
    prefix=config("commerce.endpoint.api", default="/commerce/api/v1"),
    middleware=config("commerce.middleware", default=["web"]),
)
