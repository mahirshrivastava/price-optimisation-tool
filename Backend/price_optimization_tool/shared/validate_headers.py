"""Validating headers: Content-Type, Accept"""

from flask_restful import request
from shared.custom_exception import InvalidHeaderException


def validate_headers(required_headers: dict, content_type_flag: bool = False):
    """Validating basic headers"""
    headers = request.headers
    content_type = headers.get("Content-Type", None)
    if content_type_flag and not content_type:
        raise InvalidHeaderException("Content-Type header is required!")
    if (
        content_type
        and (content_type.lower()).find(required_headers["content-type"]) == -1
    ):
        raise InvalidHeaderException("Invalid Content-Type header!")
