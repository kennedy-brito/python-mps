from Cargo import Cargo
import datetime as dt

class Funcionario():

  def __init__(self, id, nome, dataContratado: dt.date, diasFeriasMaximo, diasFeriasAtual, Cargo: Cargo) -> None:
    self.id = id
    self.nome = nome
    self.dataContratado = dataContratado
    self.diasFeriasMaximo = diasFeriasMaximo 
    self.diasFeriasAtual = diasFeriasAtual 
    self.cargo = Cargo