from abc import ABC, abstractmethod
class IDraw(ABC):
  
  @abstractmethod
  def draw(**kwarg):
    pass


class Console(IDraw):

  def draw(**kwarg):
    print("escrevendo no console")
    print(kwarg)

class TXT(IDraw):

  def draw(**kwarg):
    print("escrevendo no txt")
    print(kwarg)

class JSON(IDraw):

  def draw(**kwarg):
    print("escrevendo no json")
    print(kwarg)

class Forma():
  
  def __init__(self, posicao, p1, p2, implementa: IDraw) -> None:
    self.registrar_dados(posicao,p1,p2)
    self.metodo = implementa.draw

  def registrar_dados(self, posicao, p1,p2):
    self.posicao = posicao
    self.p1 = p1
    self.p2 = p2

  def desenhar(self):    
    self.metodo(posicao=self.posicao)
    

if __name__ == "__main__":

  circulo = Forma("quadrante 1", (0,0), (2,2), TXT)

  circulo.desenhar()

  circulo = Forma("quadrante 1", (0,0), (2,2), JSON)
  circulo.desenhar()
  
  circulo = Forma("quadrante 1", (0,0), (2,2), Console)
  circulo.desenhar()