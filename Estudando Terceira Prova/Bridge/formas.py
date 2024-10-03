from abc import ABC, abstractmethod
from api_escrita import WriteApi
class Forma(ABC):

  @abstractmethod
  def registrar_dados(self):
    pass

class Square(Forma):

  def __init__(self, lado, api: WriteApi) -> None:
    self.lado = lado
    self.api = api

  def registrar_dados(self):
    self.api.registrar(f"quadrado de lado {self.lado}")

class Circle(Forma):

  def __init__(self, raio, api: WriteApi) -> None:
    self.raio = raio
    self.api = api

  def registrar_dados(self):
    self.api.registrar(f"circulo de raio {self.raio}")


  
