from pydantic import BateModel , EmailStr

class LivroCreate(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int

class LeitorOut(BaseModel):
  codigo: int 
  preco: str 
  tipo: EmailStr
  desconto_precentual: float = 0 

class LiveroOut(BaseModel):
    codigo:int 
    titulo:str
    preco:float
    tipo:int
    desconto_precentual: float
    
