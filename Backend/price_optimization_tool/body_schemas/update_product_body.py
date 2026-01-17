from pydantic import BaseModel, Field, ConfigDict


class UpdateProductSchema(BaseModel):
    """Schema for validating update product api's body"""

    model_config = ConfigDict(extra="forbid")
    description: str = Field(min_length=1, max_length=255)
    cost_price: float = Field()
    selling_price: float = Field()
    category: str = Field( min_length=3, max_length=40)
    stock_available: int = Field()
    units_sold: int = Field()
    customer_rating: float = Field()
    demand_forecast: int = Field()
    optimized_price: float = Field()
