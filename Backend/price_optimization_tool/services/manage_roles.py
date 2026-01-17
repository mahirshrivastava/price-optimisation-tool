from ..models.user_roles_model import Roles, db


def fetch_list_of_roles():
    """Fetching list of roles"""

    roles = Roles.query.all()
    list_of_roles = []
    for role in roles:
        list_of_roles.append(serialize_roles(role))
    return list_of_roles


def add_roles(payload):
    """Fetching add roles"""
    roles = Roles(
        role_name=(payload.role_name).capitalize(),
        demand_forecast=payload.demand_forecast,
        add_products=payload.add_products,
        view_products=payload.view_products,
        update_products=payload.update_products,
        delete_products=payload.delete_products,
        optimize_price=payload.optimize_price,
        add_roles=payload.add_roles,
        update_roles=payload.update_roles,
        delete_roles=payload.delete_roles,
        add_user=payload.add_user,
        update_user=payload.update_user,
        delete_user=payload.delete_user,
    )
    db.session.add(roles)
    db.session.commit()
    return "Added new role!"


def update_roles(payload):
    """Updating roles"""
    role = Roles.query.filter_by(id=payload.id).first_or_404()
    db.session.commit()
    return "Updated role!"


def serialize_roles(roles):
    """Serializing roles"""
    return {
        "id": roles.id,
        "role_name": roles.role_name,
        "demand_forecast": roles.demand_forecast,
        "add_products": roles.add_products,
        "view_products": roles.view_products,
        "update_products": roles.update_products,
        "delete_products": roles.delete_products,
        "optimize_price": roles.optimize_price,
        "add_roles": roles.add_roles,
        "update_roles": roles.update_roles,
        "delete_roles": roles.delete_roles,
        "add_user": roles.add_user,
        "update_user": roles.update_user,
        "delete_user": roles.delete_user
    }
