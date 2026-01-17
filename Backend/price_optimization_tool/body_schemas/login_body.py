import re
from pydantic import BaseModel, Field, field_validator, ConfigDict

password_regex = re.compile(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{13,15}$'
)

email_regex = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


class LoginSchema(BaseModel):
    """Schema for validating login api's body"""

    model_config = ConfigDict(extra="forbid")
    email: str = Field(
        ..., description="Email is required!"
    )
    password: str = Field(
        ..., min_length=13, max_length=15, description="Password is required!"
    )

    @field_validator("password")
    def validate_password(cls, value):
        if not password_regex.match(value):
            raise ValueError(
                "Password must be 13-15 chars and include uppercase, lowercase, digit, and special char."
            )
        return value

    @field_validator("email")
    def validate_email(cls, value):
        if not email_regex.match(value):
            raise ValueError(
                "Invalid Email Format!"
            )
        return value
