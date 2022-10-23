from masonite.routes import Route
from masonite.configuration import config

from src.masonite_commerce.controllers.web.cart_controller import CartController
from ..controllers.web.commerce_controller import CommerceController
from ..controllers.web.product_controller import ProductController

endpoint = config("commerce.endpoint.web", default="")

ROUTES = Route.group(
    [
        Route.get("/", CommerceController.index),
        Route.get("/products", ProductController.index),
        Route.get("/products/@slug", ProductController.show),
        Route.get("/carts", CartController.index),
        Route.post("/carts", CartController.store),
        Route.post("/carts/@id", CartController.update),
        Route.delete("/carts/@id", CartController.destroy),
    ],
    prefix="" if endpoint == "/" else endpoint,
    middleware=config("commerce.middleware", default=["web"]),
)
