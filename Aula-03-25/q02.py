
# crie uma lista que recebe o quadrado dos elementos
# paralelos de l1 e l2, desde que essa soma seja impar

l1 = [13,-2,5,82,95,3,-53,12,-21]
l2 = [3,73,22,31,5,67,-3,39,-87]

power = []

# for i in range(len(l1)):
#     sumOfElement = l1[i]+l2[i]

#     if(sumOfElement % 2 != 0):
#         power.append(sumOfElement**2)

# print(power)

# Respostas do professor
# a primeira é igual a minha

# segunda forma
Lzip = list(zip(l1,l2))
print(Lzip)

Lfilter = list(filter(lambda x: (x[0]+x[1]) % 2 !=0, Lzip))

Lmap = list( map (lambda x: (x[0]+x[1])**2, Lfilter) )

print(Lmap)