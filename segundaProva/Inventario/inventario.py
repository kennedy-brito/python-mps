from .Comparators import comparador as cmp

class Inventario():

  def __init__(self) -> None:
    self.items = []

  def adicionar_item(self, item):
    self.items.append(item)

  def ordenar(self, comparador:cmp.Comparador):
    
    for _ in range(0, len(self.items)-1):

      for index in range(0, len(self.items)-1):
        item1 = self.items[index]
        item2 = self.items[index+1]
        
        if comparador.comparar(item1,item2) == 1:
          aux = item1
          self.items[index] = item2
          self.items[index+1] = aux

  def __str__(self) -> str:

    inventario = "====================\t\tItems\t\t===================="
    inventario += "\nnome \t\t\tquantidade \t\tvalor \t\tpeso"
    for item in self.items:
      novaLinha = "\n"+ str(item)
      inventario += novaLinha

    return inventario