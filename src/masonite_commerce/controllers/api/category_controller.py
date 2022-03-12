from unicodedata import category
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response

from src.masonite_commerce.constants.http_status_codes import STATUS_CREATED, STATUS_DELETED, STATUS_UPDATED
from ...models.CommerceCategory import CommerceCategory


class CategoryController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request

    def index(self):
        """ Returns a list of categories """
        
        CommerceCategory.create({
            "title": "Electronics",
            "slug": "electronics",
            "status": "published",
        })
        return CommerceCategory.paginate(10)

    def show(self, id):
        """ Returns a single category """
        
        return CommerceCategory.find(id)
    
    def store(self):
        """ Creates a new category """
        
        category = CommerceCategory.create(self.request.all())
        
        return self.response.json({
            "category": category.serialize(),
            "message": "Category created successfully"
        }, status=STATUS_CREATED)
    
    def update(self, id):
        """ Updates a category """
        
        category = CommerceCategory.find(id)
        category.update(self.request.all())
        
        return self.response.json({
            "message": "Category updated successfully"
        }, status=STATUS_UPDATED)
    
    def destroy(self, id):
        """ Deletes a category """
        category = CommerceCategory.find(id)
        category.delete()
        
        return self.response.json({
            "message": "Category deleted successfully"
        }, status=STATUS_DELETED)