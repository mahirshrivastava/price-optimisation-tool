from pydantic import BaseModel, Field, ConfigDict


class RegisterProductSchema(BaseModel):
    """Schema for validating register product api's body"""

    model_config = ConfigDict(extra="forbid")
    product_name: str = Field(..., min_length=1, max_length=40)
    description: str=Field(..., min_length=1, max_length=255)
    cost_price: float = Field(
        ...
    )
    selling_price: float = Field(
        ...
    )
    category: str= Field(..., min_length=3, max_length=40)
    available_stock: int= Field(...)
    units_sold: int = Field(...)
    customer_rating: float = Field(default=0)
    demand_forecast: int = Field(default=0)
    optimized_price: float = Field(default=0)
    
