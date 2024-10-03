from time import time, sleep
class Imagem:

  def __init__(self, nome) -> None:
    print("carregado em " + str(time()))
    self.nome = nome
    self.conteudo = [[0,0,0],[1,1,1],[2,2,2]]
    self.histograma = "histograma"

  def __str__(self) -> str:
    return str(self.nome) + "\n" + str(self.conteudo) + "\n" + str(self.histograma)

class Proxy:

  def __init__(self, nome) -> None:
    self.nome= nome
    self.arquivo = None

  def mostrar(self):
    self.arquivo = Imagem(self.nome)
    print(self.arquivo)

class Galeria:

  def __init__(self) -> None:
    self.nomes_imagens = []
    self.imagens = []

  def mostrar(self, i):
    if i >= len(self.nomes_imagens):
      return
    print(self.nomes_imagens[i])
    print(self.imagens[i].mostrar())

  def add(self, nome):
    print("adicionado em " + str(time()))
    self.nomes_imagens.append(nome)
    self.imagens.append(Proxy(nome))

if __name__ == "__main__":

  glr = Galeria()
  glr.add("imagem1")
  glr.add("imagem2")

  sleep(2)


  glr.mostrar(0)
  glr.mostrar(1)