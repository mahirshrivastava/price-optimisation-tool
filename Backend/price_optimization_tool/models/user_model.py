import bcrypt
from datetime import date
from . import db
from ..shared.global_variables import DEAFULT_ROLE


class Users(db.Model):
    """Creating database model for USERS"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    role = db.relationship("Roles", back_populates="users")
    created_by = db.Column(db.String(255), default="System")
    created_date = db.Column(db.Date, default=date.today)
    modified_date = db.Column(db.Date, default=None)

    def __repr__(self):
        """Return email"""
        return f"{self.email}"

    def set_password(self, password):
        """Setting hash password"""
        self.password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password):
        """Check provided password"""
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def set_role(self, role_name: str):
        """Setting role for user"""
        from .user_roles_model import Roles

        if not role_name or role_name.strip() == "":
            role_name = DEAFULT_ROLE or "viewer"
        default_role = Roles.query.filter_by(role_name=role_name).first()
        self.role_id = default_role.id

    @classmethod
    def get_with_role_by_email(cls, email):
        """Get user role join by email"""
        from .user_roles_model import Roles

        return (
            cls.query.join(Roles, cls.id == Roles.id)
            .filter(cls.email == email)
            .first_or_404()
        )
    
    @classmethod
    def get_with_role_by_id(cls, id):
        """Get user role join by email"""
        from .user_roles_model import Roles

        return (
            cls.query.join(Roles, cls.id == Roles.id)
            .filter(cls.id == id)
            .first_or_404()
        )
