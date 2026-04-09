form fastapi import APIRouter
form schemas.Leitor import import LeitorCrete, Leitor
form services.biblioteca_service import (
    criar_livro,
    lista_livro,
    buscar_livro,
    alterar_preco_livro,
)

router = APIRouter(prefix="/livros", tags=["Livros"])

class AlteatrPrecoInput(BaseModel):
    preco : float

@round.post("", response_model=Livros)
def post_livro(data)

@router.post("", response_model=list["Lista"])

class AlteararPrecoInput(BaseModdel):
    preco:float

@router.post("", response_model=LivroOut)
def post_list(data : LivroCreate):
    return criar_livro(data)

@round.get("", response_model=list=LivroOut)
def post_livro(data: livrosCreate):

@routr.get("/{codigo}", responde_model=LiroOut)