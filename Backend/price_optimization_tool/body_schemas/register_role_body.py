from pydantic import BaseModel, Field, ConfigDict


class AddRoleSchema(BaseModel):
    """Schema for validating register role api's body"""

    model_config = ConfigDict(extra="forbid")
    role_name: str = Field(..., min_length=1, max_length=40)
    demand_forecast: bool = Field()
    add_products: bool = Field()
    view_products: bool = Field()
    update_products: bool = Field()
    delete_products: bool = Field()
    optimize_price: bool = Field()
    add_roles: bool = Field()
    update_roles: bool = Field()
    delete_roles: bool = Field()
    add_user: bool = Field()
    update_user: bool = Field()
    delete_user: bool = Field()
    
