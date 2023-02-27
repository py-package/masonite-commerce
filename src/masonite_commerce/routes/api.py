from masonite.configuration import config
from masonite.routes import Route

from src.masonite_commerce.controllers.api.attribute_controller import (
    AttributeController,
)
from src.masonite_commerce.controllers.api.cart_controller import CartController
from src.masonite_commerce.controllers.api.category_controller import CategoryController
from src.masonite_commerce.controllers.api.comment_controller import CommentController
from src.masonite_commerce.controllers.api.customer_controller import CustomerController
from src.masonite_commerce.controllers.api.product_controller import ProductController
from src.masonite_commerce.controllers.api.tag_controller import TagController

endpoint = config("commerce.endpoint.api", default="")

ROUTES = Route.group(
    [
        # Product Routes
        Route.get("/products", ProductController.index),
        Route.post("/products", ProductController.store),
        Route.get("/products/@id:int", ProductController.show),
        Route.put("/products/@id:int", ProductController.update),
        Route.post("/products/@id:int/variations", ProductController.add_variation),
        Route.put("/products/@id:int/variations", ProductController.update_variation),
        Route.get("/products/@id:int/comments", ProductController.comments),
        # Comment Routes
        Route.get("/comments", CommentController.index),
        Route.post("/comments", CommentController.store),
        Route.delete("/comments/@id:int", CommentController.destroy),
        # Category Routes
        Route.get("/categories", CategoryController.index),
        Route.post("/categories", CategoryController.store),
        Route.put("/categories/@id", CategoryController.update),
        Route.delete("/categories/@id", CategoryController.destroy),
        # Tag Routes
        Route.get("/tags", TagController.index),
        Route.post("/tags", TagController.store),
        Route.put("/tags/@id", TagController.update),
        Route.delete("/tags/@id", TagController.destroy),
        # Cart Routes
        Route.get("/carts", CartController.index),
        Route.post("/carts", CartController.store),
        Route.put("/carts/@id", CartController.update),
        Route.delete("/carts/@id", CartController.destroy),
        # Attribute Routes
        Route.get("/attributes", AttributeController.index),
        Route.post("/attributes", AttributeController.store),
        Route.put("/attributes/@id", AttributeController.update),
        Route.delete("/attributes/@id", AttributeController.destroy),
        # Customer Routes
        Route.get("/customers", CustomerController.index),
        # Order Routes
    ],
    prefix="" if endpoint == "/" else endpoint,
    middleware=config("commerce.middleware", default=["web"]),
)
