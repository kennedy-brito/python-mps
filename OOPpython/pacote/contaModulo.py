from .pessoaModulo import ABC, abstractmethod 

class Conta(ABC):

  def __init__(self, agencia, conta, pessoa) -> None:
    
    self.pessoa = pessoa
    self.agencia = agencia
    self.conta = conta    
    self.dinheiro = 0

  @property
  def taxa(self):
    return self._taxa

  @taxa.setter
  def taxa(self, value):
    if value < 0:
      print("taxa não pode ser negativa")
      return
    
    self._taxa = value
  
  @abstractmethod
  def transferir(self, conta):
    pass

  @abstractmethod
  def depositar(self, valor):
    pass

  @abstractmethod
  def sacar(self, valor):
    pass


class Poupanca(Conta):

  def __init__(self, *args, **kwargs) -> None:
    self.taxa = 0
    super().__init__(*args, **kwargs)

  def transferir(self, conta: Conta, valor):
    
    if valor < 0:
      print("valor invalido")
      return
    
    if valor > self.dinheiro:
      print("valor insuficiente")
      return

    self.sacar(valor)
    conta.depositar(valor)

  def depositar(self, valor):
    if valor < 0:
      print("valor invalido")
      return
    
    self.dinheiro += valor

  def sacar(self, valor):
    if valor < 0:
      print("valor invalido")
      return
    
    if valor > self.dinheiro:
      print("valor insuficiente")
      return

    self.dinheiro -= valor

  
class Corrente(Conta):

  def __init__(self, *args, **kwargs) -> None:
    self.taxa = 0.15
    self.debito = 0
    super().__init__(*args, **kwargs)

  def transferir(self, conta: Conta, valor):
    
    if valor < 0:
      print("valor invalido")
      return
    
    if valor > self.dinheiro:
      print("valor insuficiente")
      return

    self.sacar(valor)
    conta.depositar(valor)
    self.debito += self.taxa
    self.pagarDebito()

  def depositar(self, valor):
    if valor < 0:
      print("valor invalido")
      return
    
    self.dinheiro += valor

  def sacar(self, valor):
    if valor < 0:
      print("valor invalido")
      return
    
    if valor > self.dinheiro:
      print("valor insuficiente")
      return

    self.dinheiro -= valor

  def pagarDebito(self):
    if self.dinheiro < self.debito:
      self.debito -= self.dinheiro
      self.dinheiro = 0
      print("Sua conta esta com saldo negativo")
      return

    self.dinheiro -= self.debito
    self.debito = 0


