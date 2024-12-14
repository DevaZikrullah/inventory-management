from pydantic import BaseModel,Field
from datetime import date
from typing import List, Annotated

class PurchaseLine(BaseModel):
    purchase_id: Annotated[int, Field(min_length=1)]
    product_id: Annotated[int, Field(min_length=1)]
    qty: Annotated[int, Field(min_length=1)]
    taxes: Annotated[float, Field(min_length=1)] 
    total: Annotated[float, Field(min_length=1)] 
    

class PurchaseSchema(BaseModel):
    purchase_number: Annotated[str, Field(min_length=1)] 
    vendor_name: Annotated[str, Field(min_length=1)] 
    order_date: date
    purchase_line: List[PurchaseLine] 