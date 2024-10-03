from app.pontoVenda import PontoVenda as pv
'''
como esse código deve funcionar?
ele é simples:
teremos opções no menu de:
  1. cadastrar produto
  2. vender produto
  3. adicionar estoque
  4. modificar produto
  5. deletar produto

nessas opções:
em 1.
  o produto deve ter:
    código:
    preço por unidade/kg
    nome
    quantidade em estoque
    preço de venda:
      calculado como 10% sobre preço por unidade

em 2. 
  ao vender, deve-se ter:
    quantidade do produto:
      pode ser um valor decimal se for produto por kg
    essa venda deve se ter em loop, até não ser informado mais nenhum código
    ou ser selecionada a opção de encerrar venda
'''

while(True):
  print(
    '''
    1. cadastrar produto
    2. vender produto
    3. adicionar estoque
    4. modificar produto
    5. deletar produto
    ''')
  opcao = input()
  pontoVenda = pv()
  match opcao:
    case "1":
      pontoVenda.addProduto()
      continue
    case "2":
      pontoVenda.vender()