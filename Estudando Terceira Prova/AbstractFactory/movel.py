from abc import ABC, abstractmethod

class Chair(ABC):
  
  @property
  def tipo(self):
    return self._tipo
  
  @tipo.setter
  def tipo(self, tipo):
    self._tipo = tipo

class Sofa(ABC):
  
  @property
  def tipo(self):
    return self._tipo
  @tipo.setter
  def tipo(self, tipo):
    self._tipo = tipo

class CoffeeTable(ABC):
  
  @property
  def tipo(self):
    return self._tipo
  @tipo.setter
  def tipo(self, tipo):
    self._tipo = tipo

class VictorianChair(Chair):

  def __init__(self) -> None:
    self.tipo = "Victorian"
  
class VictorianSofa(Sofa):

  def __init__(self) -> None:
    self.tipo = "Victorian"

class VictorianCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.tipo = "Victorian"

class ModernChair(Chair):

  def __init__(self) -> None:
    self.tipo = "Modern"
  
class ModernSofa(Sofa):

  def __init__(self) -> None:
    self.tipo = "Modern"

class ModernCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.tipo = "Modern"
  
class ArtDecoChair(Chair):

  def __init__(self) -> None:
    self.tipo = "ArtDeco"
  
class ArtDecoSofa(Sofa):

  def __init__(self) -> None:
    self.tipo = "ArtDeco"

class ArtDecoCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.tipo = "ArtDeco"
  