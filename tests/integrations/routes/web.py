from masonite.routes import Route

ROUTES = [
    # Route.get("/", "WelcomeController@show"),
    Route.get("/", "WelcomeController@commerce"),
]
