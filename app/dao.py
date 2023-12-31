from app.models import Category, Product, User
import hashlib
from app import app
def load_categories():
    return Category.query.all()


def load_products(kw=None,page=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains((kw)))

    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page-1)*page_size
        return products.slice(start, start + page_size)

    return products.all()


def count_product():
    return Product.query.count()


def get_user_by_id(id):
    return User.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()
