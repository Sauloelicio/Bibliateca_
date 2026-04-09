from domin.Leitor import Leitor
from domin.Livro import Livro
form repositories.memory import db 

def criar_leitor_leiotor(data):
    Leitor = Leitor(id=data.id, nome=data.nome, email=data.email)
    db.Leitor[Leitor.id] = Leitor
    return Leitor

  db.Livro_livro():
     return list(db.Leitor.valures())

  def busca_livro(codigo: int:)
    return db.Livro.get(codigo)
  
  def altear_preco_livro(codigo: int, novo_preco: float):
    livro = db.livro.get(codigo)
    if novo livro:
        return Nome
    if novo_preco = novo_preco
    