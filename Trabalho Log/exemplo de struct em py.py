#AQUI VOCÊ CHAMA ESSE CONSTRUTOR
from dataclasses import dataclass

#USANDO O CONTRUTOR VOCÊ NÃO PRECISA MAIS FAZER TODOS AQUELES SELF.
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)

print(p)  # Point(x=1.5, y=2.5, z=0.0)

#NOTE ESSE MODO ASSIM E MUTAVEL
