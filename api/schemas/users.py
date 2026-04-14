from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    telegram_id : Optional[int] = None
    email : Optional[str] = None
    

class UserCreate(UserBase):
    username : str
    full_name : str
    password : str

class UserOut(UserBase):
    id: int
    is_admin: bool
    created_at: datetime
    username : str
    full_name : str

    model_config = ConfigDict(from_attributes=True)