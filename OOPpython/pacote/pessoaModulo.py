from abc import ABC, abstractmethod

class Pessoa(ABC):

  def __init__(self, id, nome) -> None:
    self.id = id
    self.nome = nome

class Fisica(Pessoa):

  def __init__(self, cpf, *args, **kwargs) -> None:
    self.cpf = cpf

class Juridica(Pessoa):

  def __init__(self, cnpj, *args, **kwargs) -> None:
    self.cnpj = cnpj
    super().__init__(*args, **kwargs)