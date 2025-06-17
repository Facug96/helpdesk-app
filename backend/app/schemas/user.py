from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: Optional[str] = "employee"
class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True
class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"