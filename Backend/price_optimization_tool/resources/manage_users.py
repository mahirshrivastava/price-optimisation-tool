from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from ..body_schemas.register_body import RegisterSchema
from ..services.manage_user import register_user, fetch_user
from ..shared.custom_exception import InvalidParameterException
from ..shared.error_handler import error_handler
from ..shared.serialize_pydantic_errors import serialize_error_response
from ..shared.response import give_response
from ..shared import http_status_code as status
from ..shared.common_function import verify_user_access, verify_token_expiration


class ManageUser(Resource):
    """Class for managing users"""

    @error_handler
    def get(self):
        """"""
        email = verify_token_expiration()
        user_id = request.args.get('user_id', None)
        if user_id:
            verify_user_access(email)
        response = fetch_user(user_id=user_id, loged_user_email=email)
        return give_response(data=response)

    @error_handler
    def post(self):
        """"""
        try:
            validated_payload = RegisterSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = register_user(payload=validated_payload)
        return give_response(data=response, code=status.HTTP_201_CREATED)
