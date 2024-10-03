from Inventario import \
  Inventario, arma, consumivel, \
    comparador_peso as cp, comparador_valor as cv

inventario = Inventario()

espada =  arma.Arma(dano_base=10, durabilidade_base=15, id=1, num_items=2, valor = 13.5, nome = "espada", peso=10)

lanca =  arma.Arma(dano_base=20, durabilidade_base=10, id=2, num_items=1, valor = 17, nome = "lança", peso=15)

pocaoHp = consumivel.Consumivel(id=3, num_items=20, valor = 4.5, nome = "poção de vida", peso=1.3)
pocaoMp = consumivel.Consumivel(estragado= True, id=4, num_items=20, valor = 4.5, nome = "poção de mana", peso=1.3)
moeda = arma.Arma(dano_base=0.01, durabilidade_base=1, id=5, num_items=20, valor = 999, nome = "ouro", peso=1)

inventario.adicionar_item(espada)
inventario.adicionar_item(lanca)
inventario.adicionar_item(moeda)
inventario.adicionar_item(pocaoHp)
inventario.adicionar_item(pocaoMp)

print("\tantes de ordenar\t")
print(inventario)

print("\n\tdepois de ordenar por peso\t")
inventario.ordenar(comparador=cp.ComparadorPeso())
print(inventario)
print("\n\tdepois de ordenar por valor\t")
inventario.ordenar(comparador=cv.ComparadorValor())
print(inventario)

print("\n\nconsumindo uma poções e polindo a lança")
indice = inventario.items.index(lanca)

inventario.items[indice].polir()

indice = inventario.items.index(pocaoHp)

inventario.items[indice].comer()
inventario.items[indice].comer()
inventario.items[indice].comer()

indice = inventario.items.index(pocaoMp)
inventario.items[indice].comer()

print("\n\tdepois de consumir poções\t")
print(inventario)


