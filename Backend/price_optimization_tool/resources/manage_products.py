from pydantic import ValidationError
from flask import request
from flask_restful import Resource
from ..shared import http_status_code as status
from ..shared.error_handler import error_handler
from ..shared.common_function import (
    verify_view_product_role,
    verify_add_product_role,
    verify_token_expiration,
)
from ..shared.response import give_response
from ..shared.serialize_pydantic_errors import serialize_error_response
from ..shared.custom_exception import InvalidParameterException, AuthorizationException
from ..body_schemas.register_product_body import RegisterProductSchema
from ..body_schemas.demand_forecast_body import DemandForecastProductList
from ..services.manage_products import (
    fetch_product,
    fetch_product_list,
    register_product,
    update_product,
    delete_product,
    calculated_demand_forecast,
    calculate_optimized_price
)



class ManageProducts(Resource):
    """Get, register, updata and delete products"""

    @error_handler
    def get(self):
        """"""
        email = verify_token_expiration()
        if not email or email.strip() == "":
            raise AuthorizationException()
        verify_view_product_role(email)
        product_id = request.args.get("product_id", None)
        if not product_id:
            response = fetch_product_list(email)
        else:
            response = fetch_product(product_id=product_id, email=email)
        return give_response(data=response)

    @error_handler
    def post(self):
        """"""
        try:
            email = verify_token_expiration()
            if not email or email.strip() == "":
                raise AuthorizationException()
            verify_add_product_role(email)
            validated_payload = RegisterProductSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = register_product(validated_payload)
        return give_response(code=status.HTTP_201_CREATED, message=response, data={})

    @error_handler
    def put(self):
        """"""
        try:
            email = verify_token_expiration()
            if not email or email.strip() == "":
                raise AuthorizationException()
            verify_add_product_role(email)
            product_id = request.args.get("product_id", None)
            if not product_id or product_id.strip() == "":
                raise InvalidParameterException("Invalid product id!")
            validated_payload = RegisterProductSchema(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        response = update_product(request.json, validated_payload, product_id)
        return give_response(data={}, message=response)

    @error_handler
    def delete(self):
        """"""
        email = verify_token_expiration()
        if not email or email.strip() == "":
            raise AuthorizationException()
        verify_add_product_role(email)
        product_id = request.args.get("product_id")
        if not product_id:
            raise InvalidParameterException("Invalid query parameters!")
        response = delete_product(product_id)
        return give_response(message=response)


class ManageDemandForecast(Resource):
    """Calculated demand forecast"""

    @error_handler
    def post(self):
        """"""
        try:
            email = verify_token_expiration()
            if not email or email.strip() == "":
                raise AuthorizationException()
            verify_add_product_role(email)
            validated_payload = DemandForecastProductList(**request.json)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        reponse = calculated_demand_forecast(validated_payload.products)
        return give_response(data=reponse)
    
class ManagePrice(Resource):
    """Calculated optimized price"""

    @error_handler
    def get(self):
        """"""
        try:
            email = verify_token_expiration()
            if not email or email.strip() == "":
                raise AuthorizationException()
            verify_add_product_role(email)
        except ValidationError as error:
            list_of_errors = serialize_error_response(errors=error)
            raise InvalidParameterException(errors=list_of_errors)
        reponse = calculate_optimized_price()
        return give_response(data=reponse)
