from abc import ABC, abstractmethod
import Item
class Box(ABC):

  @property
  @abstractmethod
  def items(self):
    pass

  @abstractmethod
  def add(self, items:Item):
    pass

  @abstractmethod
  def esvaziar(self):
    pass

  @abstractmethod
  def contar(self):
    pass
