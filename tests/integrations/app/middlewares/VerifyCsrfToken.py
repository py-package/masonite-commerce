from masonite.middleware import VerifyCsrfToken as Middleware


class VerifyCsrfToken(Middleware):

    exempt = [
        "/api/v1/*"
    ]
