# config/factories.py
from masoniteorm import Factory
import random
from masonite.facades import Hash

from src.masonite_commerce.models.CommerceCategory import CommerceCategory
from src.masonite_commerce.models.CommerceProduct import CommerceProduct
from src.masonite_commerce.models.CommerceComment import CommerceComment
from tests.integrations.app.models.User import User

def user_factory(faker):
    return {
        "name": faker.unique.name(),
        "email": faker.unique.email(),
        "password": Hash.make("secret"),
        "phone": faker.phone_number(),
    }

def category_factory(faker):
    title = " ".join(faker.words(3))
    return {
        'creator_id': random.randint(1, 11),
        'title': title,
        'slug': title.lower().replace(' ', '-'),
        'status': random.choice(['draft', 'published', 'archived']),
    }
    
def product_factory(faker):
    title = " ".join(faker.words(2))
    return {
        'creator_id': random.randint(1, 11),
        'title': title,
        'slug': title.lower().replace(' ', '-'),
        'excerpt': faker.paragraph(),
        'content': '\\n'.join(faker.paragraphs(random.randint(2, 3))),
        'cover_image': faker.image_url(),
        'status': random.choice(['draft', 'published', 'archived']),
    }
    
def comment_factory(faker):
    return {
        'creator_id': random.randint(1, 11),
        'product_id': random.randint(1, 200),
        'content': '\\n'.join(faker.paragraphs(random.randint(2, 3))),
        'status': random.choice(['draft', 'published', 'archived']),
    }
    
Factory.register(User, user_factory)
Factory.register(CommerceCategory, category_factory)
Factory.register(CommerceProduct, product_factory)
Factory.register(CommerceComment, comment_factory)