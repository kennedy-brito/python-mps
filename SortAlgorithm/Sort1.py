def bubble_sort(arr: list):

  troca = True
  i = 0
  TAM = len(arr)
  while i <TAM - 1 and troca:
    troca = False
    j=0
    
    while j < TAM - 1:
      
      if arr[j] > arr[j+1]:
        troca = True
        (arr[j], arr[j+1]) = (arr[j+1], arr[j])
      
      j+=1
    
    i+=1

def merge_sort(arr: list):
  #lista auxiliar com o mesmo número de elementos
  #que a lista original
  aux:list = [_ for _ in arr]
  __mergeSort__(arr, aux)

def __mergeSort__(arr: list, aux:list, inicio = 0, fim = -1):
  fim = len(arr) -1 if fim < 0 else fim

  if fim - inicio < 1:
    return
  
  meio = inicio + (fim - inicio)//2

  __mergeSort__(arr,aux,inicio,meio)
  __mergeSort__(arr,aux,meio+1, fim)

  __Merge__(arr,aux,inicio,meio,fim)

def __Merge__(arr: list, aux:list, inicio:int, meio:int, fim:int):

  esq = inicio
  dir = meio+1

  indice = inicio

  while esq <=meio and dir <= fim:
    
    if arr[dir] < arr[esq]:
      aux[indice] = arr[dir]
      indice+=1
      dir+=1
    else:
      aux[indice] = arr[esq]
      indice+=1
      esq+=1

  while esq <= meio:
    aux[indice] = arr[esq]
    indice+=1
    esq+=1

  while dir <= fim:
    aux[indice] = arr[dir]
    indice+=1
    dir+=1
  
  # do indice de início até o indice de fim
  # o vetor aux está ordenado
  # agora é preciso substituir os valores no vetor principal
  indice = inicio
  while indice <= fim:
    arr[indice] = aux[indice]
    indice+=1

def quick_sort(arr: list, inicio = 0, fim = -1):

  fim = len(arr)-1 if fim<0 else fim

  if inicio < fim:

    pivo = __partition__(arr, inicio, fim)
    quick_sort(arr, inicio, pivo)
    quick_sort(arr, pivo+1, fim)

def __partition__(arr: list, lim_inf:int, lim_sup:int):

  pivot = arr[lim_inf]
  baixo = lim_inf
  alto = lim_sup

  while baixo < alto:

    while baixo < lim_sup and arr[baixo] <= pivot :
      baixo+=1
    
    while alto > lim_inf and arr[alto] >= pivot:
      alto-=1

    if baixo < alto:
      (arr[baixo], arr[alto]) = (arr[alto], arr[baixo])
  (arr[lim_inf], arr[alto]) = (arr[alto], pivot)
  return alto