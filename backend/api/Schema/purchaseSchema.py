from pydantic import BaseModel,Field
from datetime import date
from typing import List, Annotated

class PurchaseLine(BaseModel):
    product_id: Annotated[int, Field(ge=1)] 
    uom_id: Annotated[int, Field(ge=1)]  
    qty: Annotated[int, Field(ge=1)]  
    taxes: Annotated[float, Field(ge=0)] 
    total: Annotated[float, Field(ge=0)]    

class PurchaseSchema(BaseModel):
    purchase_number: Annotated[str, Field(min_length=1)] 
    vendor_name: Annotated[str, Field(min_length=1)] 
    order_date: date
    purchase_line: List[PurchaseLine] 