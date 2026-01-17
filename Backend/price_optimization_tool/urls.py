from flask_restful import Api
from .resources.login_user import LoginUser
from .resources.manage_users import ManageUser
from .resources.manage_products import ManageProducts, ManageDemandForecast, ManagePrice
from .resources.manage_roles import ManageRoles


def urls(api: Api):
    """Adding URLs for the application"""
    api.add_resource(LoginUser, '/api/v1/login')
    api.add_resource(ManageUser, '/api/v1/users')
    api.add_resource(ManageProducts, '/api/v1/products')
    api.add_resource(ManageRoles, '/api/v1/roles')
    api.add_resource(ManageDemandForecast, '/api/v1/demand_forecast')
    api.add_resource(ManagePrice, '/api/v1/optimized_price')