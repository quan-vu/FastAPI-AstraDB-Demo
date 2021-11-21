from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    asin: str
    title: Optional[str]


class ProductListSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    brand: Optional[str]
    country_of_origin: Optional[str]
