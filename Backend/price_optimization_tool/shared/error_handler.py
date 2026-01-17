"""Error handler"""

import traceback
from jwt.exceptions import ExpiredSignatureError
from flask_jwt_extended.exceptions import NoAuthorizationError
from . import http_status_code as status
from .response import give_response
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from .custom_exception import (
    InternalError,
    InvalidParameterException,
    KeyErrorException,
    ValueErrorException,
    TypeErrorException,
    AuthorizationException,
    InvalidHeaderException,
    AuthenticationException,
)
from ..log import logger


def error_handler(func):
    """
    Decorator to handle common exceptions in resources
    """

    def func_wrapper(*args, **kwargs):
        """
        Function wrapper
        """
        try:
            return func(*args, **kwargs)
        except NotFound as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message="Invalid User!",
                    code=status.HTTP_404_NOT_FOUND,
                    success=False,
                ),
                status.HTTP_404_NOT_FOUND,
            )
        except IntegrityError as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message="Duplicated entry!",
                    code=status.HTTP_409_CONFLICT,
                    success=False,
                ),
                status.HTTP_409_CONFLICT,
            )
        except NoAuthorizationError as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message="Invalid authorization token!",
                    code=status.HTTP_403_FORBIDDEN,
                    success=False,
                ),
                status.HTTP_403_FORBIDDEN,
            )
        except ExpiredSignatureError as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message="Token is expired, retry login!",
                    code=status.HTTP_403_FORBIDDEN,
                    success=False,
                ),
                status.HTTP_403_FORBIDDEN,
            )
        except KeyErrorException as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error.message)}")
            response = (
                give_response(
                    message=str(error.message), code=int(error.code), success=False
                ),
                error.code,
            )
        except (ValueErrorException, TypeErrorException) as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error.message)}")
            response = (
                give_response(
                    message=str(error.message), code=int(error.code), success=False
                ),
                error.code,
            )
        except InternalError as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error.message)}")
            response = (
                give_response(
                    message=str(error.message),
                    code=int(error.code),
                    success=False,
                ),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except InvalidParameterException as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    data=error.data,
                    message=error.message,
                    code=error.code,
                    success=False,
                    errors=error.errors,
                ),
                error.code,
            )
        except AuthenticationException as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message=error.message,
                    code=error.code,
                    success=False,
                ),
                error.code,
            )
        except AuthorizationException as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message=error.message,
                    code=error.code,
                    success=False,
                ),
                error.code,
            )
        except InvalidHeaderException as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(message=error.message, code=error.code, success=False),
                status.HTTP_406_NOT_ACCEPTABLE,
            )
        except Exception as error:
            logger.error(f"{traceback.format_exc()}")
            logger.error(f"error is {str(error)}")
            response = (
                give_response(
                    message="Internal Error",
                    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    success=False,
                ),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return response

    return func_wrapper
