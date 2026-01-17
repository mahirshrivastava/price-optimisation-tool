from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from ..body_schemas.register_role_body import AddRoleSchema
from ..shared.error_handler import error_handler
from ..shared.common_function import (
    verify_token_expiration,
    verify_update_role,
    verify_add_role,
)
from ..shared.response import give_response
from ..shared.serialize_pydantic_errors import serialize_error_response
from ..shared.custom_exception import InvalidParameterException
from ..shared import http_status_code as status
from ..services.manage_roles import fetch_list_of_roles, add_roles, update_roles


class ManageRoles(Resource):
    """Adding new custom roles with access to different features"""

    @error_handler
    def get(self):
        """"""
        email = verify_token_expiration()
        verify_add_role(email)
        response = fetch_list_of_roles()
        return give_response(data=response)

    @error_handler
    def post(self):
        """"""
        try:
            email = verify_token_expiration()
            verify_add_role(email)
            validated_payload = AddRoleSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = add_roles(validated_payload)
        return give_response(code=status.HTTP_201_CREATED, message=response)

    @error_handler
    def patch(self):
        """Updating required field"""
        try:
            email = verify_token_expiration()
            verify_update_role(email)
            validated_payload = AddRoleSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = update_roles(validated_payload)
        return give_response(code=status.HTTP_200_OK, message=response)