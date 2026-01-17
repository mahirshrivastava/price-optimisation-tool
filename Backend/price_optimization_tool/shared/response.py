"""create response for api"""
from datetime import datetime


def give_response(
    message="operation successful", data="No data found", code=200, success=True, errors=[]
):
    """
    :param message: To tell whether the operation goes fine or not
    :param data: We have to pass to the request
    :param code: Operation code
    :param success: True or False
    :return: Response for the api
    """
    timestamp = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    response = {
        "data": data,
        "code": code,
        "success": success,
        "message": message,
        "timestamp": timestamp,
    }
    if (len(errors) > 0):
        response["errors"] = errors
    if (success == False):
        return response
    return response, code
