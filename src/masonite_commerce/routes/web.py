from masonite.routes import Route
from masonite.configuration import config
from ..controllers.web.commerce_controller import CommerceController


ROUTES = Route.group(
    [Route.get("/", CommerceController.index)],
    prefix=config("commerce.endpoint.web", default="/commerce"),
    middleware=config("commerce.middleware", default=["web"]),
)
