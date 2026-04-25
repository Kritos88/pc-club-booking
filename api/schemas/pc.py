from pydantic import BaseModel, ConfigDict

class PCBase(BaseModel):
    name : str
    status : str = 'free'
    price_per_hour : int

class PCOut(PCBase):
    id : int
    model_config = ConfigDict(from_attributes=True)
    
class PCCreate(PCBase):
    pass