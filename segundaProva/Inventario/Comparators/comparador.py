from  abc import ABC, abstractmethod

class Comparador(ABC):

  @staticmethod
  @abstractmethod
  def comparar(item1, item2):
    pass