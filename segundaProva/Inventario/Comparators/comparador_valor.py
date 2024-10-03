from .comparador import Comparador

class ComparadorValor(Comparador):
  
  @staticmethod
  def comparar(item1, item2):
    return item1.valor>item2.valor

