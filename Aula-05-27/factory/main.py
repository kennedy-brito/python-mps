from factory import *
from moveis import *
def createChair(factory : FurnitureFactory):

  return factory.createChair()
def createSofa(factory : FurnitureFactory):

  return factory.createChair()
def createCoffeeTable(factory : FurnitureFactory):

  return factory.createChair()
repete = True
while(repete):

  escolha = int(input())
  
  match(escolha):
    case 1:
      objeto = createChair(VictorianFactory)
    case 2:
      objeto = createSofa(ModernFactory)
    case 3:
      objeto = createCoffeeTable(ArtDecoFactory)
    case 4:
      repete = False
  
  print(objeto.movel)
