from pydantic import BaseModel,Field
from datetime import date
from typing import List, Annotated

class LocationSchema(BaseModel):
    location_name: Annotated[str, Field(min_length=1)] 
    short_name: Annotated[str, Field(min_length=1)] 
