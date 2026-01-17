"""Custom exception"""


class InternalError(Exception):
    """
    raised for db or calculation related problems
    """

    def __init__(self, message: str, code: int):
        super().__init__(message, code)
        self.message = message
        self.code = code

    def __str__(self):
        return f"{repr(self.message)}, {repr(self.code)}"


class AuthenticationException(Exception):
    """
    Raise when Authentication error 
    """

    def __init__(
        self,
        message: str = "Unauthenticated",
        code: int = 401,
        data: dict = {},
        errors: list = [],
    ):
        super().__init__(message, code)
        if data is None:
            data = {}
        self.code = code
        self.message = message
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class InvalidParameterException(Exception):
    """
    Raise when invalid parameter passes
    """

    def __init__(
        self,
        message: str = "Invalid parameters!",
        code: int = 400,
        data: dict = {},
        errors: list = [],
    ):
        super().__init__(message, code)
        if data is None:
            data = {}
        self.code = code
        self.message = message
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class InvalidHeaderException(Exception):
    """
    Raise when invalid header passes
    """

    def __init__(self, message: str, code: int = 406, data: dict = None):
        super().__init__(message, code)
        if data is None:
            data = {}
        self.code = code
        self.message = message
        self.data = data

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class ValueErrorException(Exception):
    """
    Raise on value error
    """

    def __init__(self, message: str, code: int = 500):
        super().__init__(message, code)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class TypeErrorException(Exception):
    """
    Raise on type error
    """

    def __init__(self, message: str, code: int = 500):
        super().__init__(message, code)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class KeyErrorException(Exception):
    """
    Raise on Key error
    """

    def __init__(self, message: str, code: int):
        super().__init__(message, code)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"


class AuthorizationException(Exception):
    """
    Raise on Authorization error
    """

    def __init__(self, message: str = "Unauthorised to perform this action!", code: int = 403):
        super().__init__(message, code)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"{repr(self.message)}, {repr(self.code)}"
