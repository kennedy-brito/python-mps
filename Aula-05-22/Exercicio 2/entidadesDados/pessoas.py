from datetime import date as dt

class Funcionario():

  def __init__(self, id, nome, Cargo, id_projeto) -> None:
    self.id = id
    self.nome = nome
    self.cargo = Cargo
    self.id_projeto = id_projeto

class Cliente():

  def __init__(self, id, nome, id_projeto) -> None:
    self.id = id
    self.nome = nome
    self.id_projeto = id_projeto

  def __class__(self):
    return "cliente"
