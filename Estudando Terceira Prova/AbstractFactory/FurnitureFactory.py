from abc import ABC, abstractmethod
from movel import *
class FurnitureFactory(ABC):

  @classmethod
  @abstractmethod
  def createChair():
    pass
  
  @classmethod
  @abstractmethod
  def createSofa():
    pass

  @classmethod
  @abstractmethod
  def createCoffeeTable():
    pass


class VictorianFactory(FurnitureFactory):
  
  @staticmethod
  def createChair():
    return VictorianChair()

  @staticmethod
  def createSofa():
    return VictorianSofa()

  @staticmethod
  def createCoffeeTable():
    return VictorianCoffeeTable()

class ArtDecoFactory(FurnitureFactory):
  
  @staticmethod
  def createChair():
    return ArtDecoChair()

  @staticmethod
  def createSofa():
    return ArtDecoSofa()

  @staticmethod
  def createCoffeeTable():
    return ArtDecoCoffeeTable()
  
class ModernFactory(FurnitureFactory):
  
  @staticmethod
  def createChair():
    return ModernChair()

  @staticmethod
  def createSofa():
    return ModernSofa()

  @staticmethod
  def createCoffeeTable():
    return ModernCoffeeTable()


