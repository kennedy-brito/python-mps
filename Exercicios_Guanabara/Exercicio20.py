import random

names = []
for i in range(0,4):
  student = input(f"digite o nome do aluno {i+1}")
  names.append(student)

for i in range(0,4):
  randomStudent = random.randint(0, len(names)-1)
  print(f"A {i+1}ª apresentação será de: {names[randomStudent]}")
  names.remove(names[randomStudent])