  
from Sort1 import *
from Sort2 import *
from random import randint
from datetime import timedelta
from timeit import default_timer as timer 

def test(arr: list, tipo: str):

  #copiando a lista
  metodos = [\
    bubble_sort,
    merge_sort,
    # quick_sort,
    insertion_sort,
    shell_sort,
    straigh_sort,
    heap_sort
      ]
  # print(f"vetor antes \n{arr}")
  print(f"=================={tipo}==================")
  print("metodo\t\t|tamanho\t|tempo\n")
  for metodo in metodos:
    copia = [i for i in arr]
    executar(copia, metodo, tipo)


def executar(arr: list, metodo, tipo:str):

  start_time = timer()
  metodo(arr)
  end_time = timer()

  tempo = timedelta(seconds=end_time - start_time)
  print(f"{metodo.__name__}\t|{len(arr)}\t\t|{tempo}")


size = 1

arr = []
num_elementos = [10, 100, 1_000, 10_000, 100_000]
for tamanho in num_elementos:
  
  arr = [randint(-100,100) for _ in range(0, tamanho)]
  test(arr, "desordenado")
  
  # arr = [ i for i in range(0, tamanho)]
  # test(arr, "ordenado")

  # arr = [ tamanho - i for i in range(0, tamanho)]
  # test(arr, "invertido")