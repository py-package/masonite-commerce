from enum import Enum


class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    UPDATED = 202
    DELETED = 204
    NOT_FOUND = 404
    UNPROCESSABLE = 422
