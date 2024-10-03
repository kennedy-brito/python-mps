import Funcionario as F
from Funcionario import dt

if __name__ == "__main__":

  gerente = F.Cargo(1, "gerente", 7000)

  funcionario = F.Funcionario(1, "Zezinho", dt.date(1998, 6, 22), 30, 20, gerente)

  print("id: ", funcionario.id)
  print("nome: ", funcionario.nome)
  print("data Contratado: ", funcionario.dataContratado.strftime("%d/%m/%Y"))
  print("dias FeriasAtual: ", funcionario.diasFeriasAtual)
  print("dias FeriasMaximo: ", funcionario.diasFeriasMaximo)
  print("id do Cargo: ", funcionario.cargo.id)
  print("nome do Cargo: ", funcionario.cargo.nome)
  print("salario do Cargo: ", funcionario.cargo.salario)