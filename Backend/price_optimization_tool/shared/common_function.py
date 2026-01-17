from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..models.user_model import Users
from ..models.user_roles_model import Roles
from ..shared.custom_exception import AuthorizationException


def verify_token_expiration():
    """Verify token if not verify return email"""
    verify_jwt_in_request()
    user = get_jwt_identity()
    users = Users.query.filter_by(email=user).first_or_404()
    if not users:
        raise AuthorizationException()
    return user


def verify_add_product_role(email):
    """Verifing add product role"""
    user = Users.get_with_role_by_email(email)
    if user.role.add_products:
        return user
    raise AuthorizationException()


def verify_view_product_role(email):
    """checking viewer role"""
    user = Users.get_with_role_by_email(email)
    if user.role.view_products:
        return True
    raise AuthorizationException()


def verify_add_role(email):
    """checking for adding role"""
    user = Users.get_with_role_by_email(email)
    if user.role.add_roles:
        return True
    raise AuthorizationException()

def verify_update_role(email):
    """checking for updating role"""
    user = Users.get_with_role_by_email(email)
    if user.role.update_roles:
        return True
    raise AuthorizationException()


def verify_user_access(email):
    """Verifing user access"""
    user = Users.get_with_role_by_email(email)
    if user.role.add_user:
        return True
    raise AuthorizationException()


def verify_user_delete_access(email):
    """User delete access"""
    user = Users.get_with_role_by_email(email)
    if user.role.delete_user:
        return True
    raise AuthorizationException()
