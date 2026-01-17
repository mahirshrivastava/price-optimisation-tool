from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .product_model import Products
from .user_model import Users
from .user_roles_model import Roles