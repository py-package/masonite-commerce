from masonite.routes import Route
from masonite.configuration import config

from src.masonite_commerce.controllers.api.category_controller import CategoryController
from src.masonite_commerce.controllers.api.product_controller import ProductController


ROUTES = Route.group(
    [
        # Product Routes
        Route.get("/products", ProductController.index),
        # Category Routes
        Route.get("/categories", CategoryController.index),
    ],
    prefix=config("commerce.endpoint.api", default="/commerce/api/v1"),
    middleware=config("commerce.middleware", default=["web"]),
)
