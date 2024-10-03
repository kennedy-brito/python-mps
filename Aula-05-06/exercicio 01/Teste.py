from Item import Item
from ListBox import ListBox
from DictBox import DictBox
"""
this function return a list
of boxes
these boxes are ListBox
"""
def repack_boxes(*args):
  # allListBox = []
  # allDictBox = []
  numberItems = 0
  for i in args:
    numberItems+= len(i.items)
  
  itemsPerBox = numberItems/len(args)
  boxes = []
  items = []
  for i in args:
    if type(i) == ListBox:
      print("Box de List")
  # print(itemsPerBox)




listItems = [Item(i,i**2) for i in range(0,10)]

dictItems = {i: Item(i,i**2) for i in range(0,10)}

listBox = ListBox()

print('*'*5,"caixa de listas",'*'*5)
listBox.add(listItems)

for i in listBox.items:
  print(i.valor)

print(listBox.contar())

print()
print('*'*5,"caixa de dicionários",'*'*5)
dictBox = DictBox()
dictBox.add(dictItems)

for i in dictBox.items:
  print(dictBox.items[i].valor)



print()
print('*'*5,"repack boxes",'*'*5)
repack_boxes(dictBox,listBox)


