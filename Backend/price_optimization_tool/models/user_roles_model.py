from datetime import date
from . import db


class Roles(db.Model):
    """Database model for USER's ROLE"""

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    role_name = db.Column(db.String(30), nullable=False, unique=True, index=True)
    demand_forecast = db.Column(db.Boolean, default=False)
    add_products = db.Column(db.Boolean, default=False)
    view_products = db.Column(db.Boolean, default=False)
    update_products = db.Column(db.Boolean, default=False)
    delete_products = db.Column(db.Boolean, default=False)
    optimize_price = db.Column(db.Boolean, default=False)
    add_roles = db.Column(db.Boolean, default=False)
    update_roles=db.Column(db.Boolean, default=False)
    delete_roles=db.Column(db.Boolean, default=False)
    add_user=db.Column(db.Boolean, default=False)
    update_user=db.Column(db.Boolean, default=False)
    delete_user=db.Column(db.Boolean, default=False)
    users = db.relationship("Users", back_populates="role")
    created_by=db.Column(db.String(255), default="System")
    created_date=db.Column(db.Date, default=date.today)
    modified_date=db.Column(db.Date, default=None)

    def __repr__(self):
        return f"<Role {self.role_name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "role_name": self.role_name,
            "demand_forecast": self.demand_forecast,
            "add_products": self.add_products,
            "view_products": self.view_products,
        }
