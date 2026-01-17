from pydantic import ValidationError


def serialize_error_response(errors: ValidationError):
    """Serializing errors coming from pydantic"""
    response_obj = []
    for error in errors.errors():
        response_obj.append({"field": error["loc"][0], "message": error["msg"]})
    return response_obj
