from flask_jwt_extended import create_access_token
from ..models.user_model import Users, db
from ..shared.custom_exception import InvalidParameterException, AuthenticationException


def login_user(payload):
    """Validating user"""
    users = Users.query.filter_by(email=payload.email).first_or_404()
    if not users:
        raise InvalidParameterException("Invalid Email or Password!")
    authenticate_password = users.check_password(payload.password)
    if not authenticate_password:
        raise AuthenticationException(
            errors=[{"field": "password", "message": "Invalid password!"}]
        )
    access_token = create_access_token(identity=payload.email)
    return {"access_token": access_token}


def register_user(payload):
    """Registering User"""
    user = Users(
        first_name=payload.first_name, last_name=payload.last_name, email=payload.email
    )
    user.set_password(payload.password)
    user.set_role(role_name="")
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=payload.email)
    return {"access_token": access_token}


def fetch_user(user_id, loged_user_email):
    """Fetch users based on product id and list of users"""
    if user_id:
        user = Users.get_with_role_by_id(user_id)
    else:
        user = Users.get_with_role_by_email(loged_user_email)
    return user_object_serialization(user)


def user_object_serialization(user):
    """Serializing user object"""
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role": user.role.role_name,
        "demand_forecast": user.role.demand_forecast,
        "add_products": user.role.add_products,
        "view_products": user.role.view_products,
        "update_products": user.role.update_products,
        "delete_products": user.role.delete_products,
        "optimize_price": user.role.optimize_price,
        "add_roles": user.role.add_roles,
        "update_roles": user.role.update_roles,
        "delete_roles": user.role.delete_roles,
        "add_user": user.role.add_user,
        "update_user": user.role.update_user,
        "delete_user": user.role.delete_user,
    }
