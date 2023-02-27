from masonite.configuration import config
from masonite.routes import Route

from src.masonite_commerce.controllers.dashboard.dashboard_controller import DashboardController

endpoint = config("commerce.endpoint.dashboard", default="")

ROUTES = Route.group(
    [
        Route.get("/", DashboardController.index),
    ],
    prefix="" if endpoint == "/" else endpoint,
    middleware=config("commerce.middleware", default=["web"]),
)
