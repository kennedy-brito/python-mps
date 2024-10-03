import math

oposto = float(input("digite o cateto oposto"))
adjacente = float(input("digite o cateto adjacente"))

hipotenusa = math.sqrt(oposto**2+adjacente**2)

print("hipotenusa do triangulo é {}".format(hipotenusa))