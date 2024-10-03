from abc import ABC, abstractmethod

class WriteApi(ABC):

  @abstractmethod
  def registrar(self, message):
    pass

class WriteConsole(WriteApi):
  
  def registrar(self, message):
    print("escrevendo no Console: " + message)

class WriteTxt(WriteApi):
  
  def registrar(self, message):
    print("escrevendo num txt: " + message)

class WriteJson(WriteApi):
  
  def registrar(self, message):
    print("escrevendo num Json: " + message)


