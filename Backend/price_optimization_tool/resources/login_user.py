from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from ..body_schemas.login_body import LoginSchema
from ..services.manage_user import login_user
from ..shared.response import give_response
from ..shared.custom_exception import InvalidParameterException
from ..shared.serialize_pydantic_errors import serialize_error_response
from ..shared.error_handler import error_handler


class LoginUser(Resource):
    """Login User"""

    @error_handler
    def post(self):
        """"""
        try:
            validated_payload = LoginSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = login_user(payload=validated_payload)
        return give_response(data=response)
