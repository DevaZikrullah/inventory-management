from pydantic import BaseModel,Field
from datetime import date
from typing import List, Annotated

class PurchaseLine(BaseModel):
    item_name: Annotated[str, Field(min_length=1)]  # Ensure it's a non-empty string
    quantity: Annotated[int, Field(ge=0)]  # Ensure non-negative quantity
    price: Annotated[float, Field(ge=0)]  # Ensure non-negative price

# Define the main purchase schema
class PurchaseSchema(BaseModel):
    purchase_number: Annotated[str, Field(min_length=1)]  # Ensure it's a non-empty string
    vendor_name: Annotated[str, Field(min_length=1)]  # Ensure it's a non-empty string
    order_date: date
    purchase_line: List[PurchaseLine]  # A list of PurchaseLine objects