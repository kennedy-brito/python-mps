from Roda import Roda
from typing import List

class Veiculo:
  
  def __init__(self, fabricante:str, modelo:str, ano:int, rodas: List[Roda]) -> None:
    self.fabricante = fabricante
    self.modelo = modelo
    self.ano = ano
    self.rodas = rodas

  def acelerar(tempo: int, rpm: int) -> int:
    pass