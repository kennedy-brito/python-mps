frase = "Um pequeno jabuti xereta viu dez cegonhas felizes."

def limitColumns(frase:str, maxColumns:int):
  word = []

  word = frase.split(' ')

  columnCount = 0;

  for i in word:
    if(columnCount + i.__len__() + 1> maxColumns):
      columnCount = 0;
      print(end="\n")

    print(i, end=" ")
    columnCount+=i.__len__()

limitColumns(frase, 20)
