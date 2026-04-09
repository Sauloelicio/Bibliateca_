from pydatic import BaseModel, EmailStr

class LeitorCreate(Basemodel):
    id: int
    nome: str
    email: EmailStr

class LeitorOut(BaseModel):
    id: int 
    nome: str 
    email: EmailStr

