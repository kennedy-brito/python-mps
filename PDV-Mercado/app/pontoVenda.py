from app.produto import Produto, ProdutoVendido

class PontoVenda():

  def __init__(self) -> None:
    self.produtos = []

  def addProduto(self):
    print("Preço por Unidade:")
    precoUnidade = float(input())
    print("Código: ")
    codigo = input()
    print("Nome: ")
    nome = input()
    print("Quantidade: ")
    qnt = input()

    produto = Produto(codigo, precoUnidade,nome ,qnt )
    self.produtos.append(produto)
  
  def vender(self):

    produtosVendidos = []

    while(True):
      dados = input("quantidade vendida do produto: quantidade*código")

      if(dados == "vender"):
        break;
      
      dados.replace(",",".")

      (quantidade, codigo) = dados.split("*")
      

      produto = self.procurarProduto(codigo)

      if(not produto and type(produto) == bool):
        print("produto não encontrado")
        continue
      
      produtosVendidos.append(
        ProdutoVendido(codigo, produto.nome, quantidade, produto.precoVenda)
      )  

      print("para sair da venda, insira vender no código do produto")
    
    print("código\t\tproduto\t\tquantidade\t\tpreço")
    precoTotal = 0
    for produto in produtosVendidos:
      precoVenda = produto.quantidade*produto.precoUnidade
      precoTotal = precoVenda
      print(f"{produto.codigo}\t\t{produto.nome}\t\t{produto.quantidade}\t\{produto.precoUnidade} = R${precoVenda}")

  
  def procurarProduto(self, codigo) -> (bool | Produto):
    
    return next((item for item in self.produtos if item.codigo == codigo), False)