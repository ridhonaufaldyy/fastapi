from pydantic import BaseModel

class UserCreate(BaseModel):
    fullname: str
    nik: str
    email: str
    telp: str
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    fullname: str
    nik: str
    email: str
    telp: str
    username: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None
