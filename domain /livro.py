class Livro: 
    def __init__ (self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percentual : float = 0):
        if preco < 0 :
            raise ValueError("O PREÇO não pode ser negativo")
        if desconto_percentual < 0 or desconto_percentual > 100:
            raise ValueError("o desconto deve estar 0 e 100.")
        if tipo not in [1,2]:
            raise ValueError("tipo invalido. Use 1 para gratuito e 2 para pago")

            self.codigo = codigo
            self.titulo = titulo
            self.preco = preco
            self.desconto_percentual = desconto_percentual

    def preco_final(self) -> float:
     id self.tipo == 1:
       return 0.0 
       desconto = self.preco * (self.desconto_percentual / 100)
       return round(self.preco - desconto, 2)
       