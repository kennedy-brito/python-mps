from pacote import p, c

pessoa1 = p.Fisica("012.123.123-12", id=1, nome="joao")

poupanca = c.Poupanca(agencia="907.3", conta="38.087", pessoa=pessoa1)
corrente = c.Corrente(agencia="907.3", conta="38.087", pessoa=pessoa1)

print(poupanca.taxa)
print(poupanca.dinheiro)
poupanca.depositar(1000)
print(poupanca.dinheiro)
poupanca.sacar(500)
print(poupanca.dinheiro)
poupanca.transferir(corrente, 500)
print(poupanca.dinheiro)

print("Corrente")
print(corrente.dinheiro)
