from masonite.routes import Route
from masonite.configuration import config

from src.masonite_commerce.controllers.web.cart_controller import CartController
from ..controllers.web.commerce_controller import CommerceController


ROUTES = Route.group(
    [
        Route.get("/", CommerceController.index),
        Route.get("/products", CommerceController.products),
        Route.get("/products/@slug", CommerceController.show),
        Route.get("/carts", CartController.index),
        Route.post("/carts", CartController.add_to_cart),
    ],
    prefix=config("commerce.endpoint.web", default="/commerce"),
    middleware=config("commerce.middleware", default=["web"]),
)
