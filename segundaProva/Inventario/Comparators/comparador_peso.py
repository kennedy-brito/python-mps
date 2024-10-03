from .comparador import Comparador

class ComparadorPeso(Comparador):
  
  @staticmethod
  def comparar(item1, item2):
    return item1.peso > item2.peso

