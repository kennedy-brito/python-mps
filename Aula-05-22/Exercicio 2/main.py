from entidadesDados.pessoas import Cliente, Funcionario
from entidadesDados.trabalho import Cargo, Projeto
from discoUtils.Writer import Writer
from discoUtils.Reader import Reader

if __name__ == "__main__":

  gerente = Cargo(1, "gerente", 8000)
  arquiteto = Cargo(2, "arquiteto", 5000)

  casa = Projeto(3, 1_000_000)
  predio = Projeto(4, 800_000_000)

  funcionario1 = Funcionario(5, "zezao", gerente, 3)
  funcionario2 = Funcionario(6, "zezinho", arquiteto, 4)

  cliente1 = Cliente(10, "joao", 3)
  cliente2 = Cliente(11, "gabriel", 4)
  
  Writer.writeJson(cliente2)

  jsonRead = Reader.readJson(f"{cliente2.__class__()}_{cliente2.id}.json")

  print(jsonRead)