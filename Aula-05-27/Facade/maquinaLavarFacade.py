from enxaguante import Enxaguante
from lavador import Lavador
from secador import Secador

class Maquina():

  def __init__(self) -> None:
    self.secador = Secador()
    self.lavador = Lavador()
    self.enxaguante = Enxaguante()

  def lavagemCompleta(self):
    self.lavar()
    self.enxaguar()
    self.secar()

  def secar(self):
    self.secador.usando()

  def lavar(self):
    self.lavador.usando()

  def enxaguar(self):
    self.enxaguante.usando()