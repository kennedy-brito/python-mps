import random

names = []
for i in range(0,4):
  student = input(f"digite o nome do aluno {i+1}")
  names.append(student)

randomStudent = random.randint(0,3)

print(f"o aluno sorteado foi {names[randomStudent]}")