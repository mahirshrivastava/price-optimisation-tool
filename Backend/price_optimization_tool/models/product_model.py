from . import db
from datetime import date


class Products(db.Model):
    """Creating database model for Products"""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_name = db.Column(db.String(40), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=False)
    cost_price = db.Column(db.Float, nullable=False)
    selling_price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(40), nullable=False)
    stock_available = db.Column(db.Integer, nullable=False)
    units_sold = db.Column(db.Integer, nullable=False)
    customer_rating = db.Column(db.Float, nullable=False, default=0)
    demand_forecast = db.Column(db.Integer, default=0)
    optimized_price = db.Column(db.Float, default=None)
    created_by = db.Column(db.String(255), default="System")
    created_date = db.Column(db.Date, default=date.today)
    modified_date = db.Column(db.Date, default=None)
