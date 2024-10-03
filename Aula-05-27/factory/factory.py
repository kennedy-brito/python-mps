from abc import ABC, abstractmethod
from moveis import *
class FurnitureFactory(ABC):

  @staticmethod
  @abstractmethod
  def createChair() ->Chair:
    pass

  @staticmethod
  @abstractmethod
  def createSofa() ->Sofa:
    pass 
  
  @staticmethod
  @abstractmethod
  def createCoffeeTable() ->CoffeeTable:
    pass 

class VictorianFactory(FurnitureFactory):
  
  @staticmethod
  def createChair() -> Chair:
    return VictorianChair()

  @staticmethod
  def createSofa() -> Sofa:
    return VictorianSofa()

  @staticmethod
  def createCoffeeTable() -> CoffeeTable:
    return VictorianCoffeeTable()
 
class ArtDecoFactory(FurnitureFactory):
  @staticmethod
  def createChair() -> Chair:
    return ArtDecoChair()

  @staticmethod
  def createSofa() -> Sofa:
    return ArtDecoSofa()

  @staticmethod
  def createCoffeeTable() -> CoffeeTable:
    return ArtDecoCoffeeTable()
 
class ModernFactory(FurnitureFactory):
  @staticmethod
  def createChair() -> Chair:
    return ModernChair()

  @staticmethod
  def createSofa() -> Sofa:
    return ModernSofa()

  @staticmethod
  def createCoffeeTable() -> CoffeeTable:
    return ModernCoffeeTable()
 
