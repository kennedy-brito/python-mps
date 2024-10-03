from abc import ABC, abstractmethod

class Item(ABC):

  def __init__(self, num_items:int, id:int, valor: float, nome:str, peso:float):
    self.id = id
    self.num_items = num_items
    self.valor = valor
    self.nome = nome
    self.peso = peso

  @abstractmethod
  def usar(self):
    pass

  @abstractmethod
  def __str__(self) -> str:
    pass

  @property
  def num_items(self):
    return self._num_items
  
  @num_items.setter
  def num_items(self, quantidade):
    self._num_items = quantidade
    
  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def valor(self):
    return self._valor

  @valor.setter
  def valor(self, value):
    if value <0:
      print("Um item não pode ter valor negativo")
      return
    self._valor = value

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, value):
    self._nome = value

  @property
  def peso(self):
    return self._peso

  @peso.setter
  def peso(self, value):
    if value <0:
      print("Um item não pode ter peso negativo")
      return
    self._peso = value

  