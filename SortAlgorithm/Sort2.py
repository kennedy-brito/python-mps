def insertion_sort(arr: list):

  for i in range(1, len(arr)):

    elemento = arr[i]

    j = i -1
    
    while j >= 0 and arr[j] > elemento:

      arr[j+1] = arr[j]
      j-=1
    
    arr[j+1] = elemento

def shell_sort(arr: list):
  k = 1

  while k < len(arr) //3 :
    k = 3*k+1

  while k >0:

    for i in range(k, len(arr)):
      aux = arr[i]
      j = i
      
      while j >= k and arr[j-k] > aux:

        arr[j] = arr[j-k]
        j = j-k
      
      arr[j] = aux
    
    k = (k - 1)//3

def straigh_sort(arr: list):

  for indice in range(0, len(arr) -1):

    menor = indice

    for atual in range(indice+1, len(arr)):

      if arr[atual] < arr[menor]:
        menor = atual
    
    (arr[menor], arr[indice]) = (arr[indice], arr[menor])

def heap_sort(arr: list):

  tam = len(arr)
  indice = tam // 2 -1
  while indice>=0:
    __heapify__(arr, tam, indice)
    indice-=1


def __heapify__(arr, tam_heap, indice_raiz):

  maior = indice_raiz
  filho_esq = 2*indice_raiz + 1
  filho_dir = 2*indice_raiz + 2

  while True:

    if filho_esq < tam_heap and arr[filho_esq] > arr[maior]:
      maior = filho_esq
    
    if filho_dir < tam_heap and arr[filho_dir] > arr[maior]:
      maior = filho_dir

    if maior != indice_raiz:
      (arr[indice_raiz], arr[maior]) = (arr[maior], arr[indice_raiz])

      # atualiza os indices
      indice_raiz = maior

      filho_esq = 2*indice_raiz + 1
      filho_dir = 2*indice_raiz + 2
    else:
      break
    
