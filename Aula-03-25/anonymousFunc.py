
# Crie uma função anônima que some dois valores caso a soma seja menor
# ou igual a 0 e multiplica os dois valores caso contrário

func = lambda x, y: x*y if x+y <=0 else x+y

print(func(2,-11))