from dataclasses import dataclasses

@dataclasses(frazen=True)
class Leitor:
    id : int 
    nome : str
    email: str
    