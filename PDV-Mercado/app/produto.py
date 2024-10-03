class Produto():

  def __init__(self, codigo, precoUnidade, nome, qnt):
    self.precoUnidade = precoUnidade
    self.codigo = codigo
    self.nome = nome
    self.qnt = qnt
    self.precoVenda = precoUnidade*1.1

class ProdutoVendido:
  def __init__(self, codigo, nome, quantidade, precoUnidade) -> None:
    self.codigo = codigo
    self.nome = nome
    self.qnt = quantidade
    self.precoUnidade = precoUnidade