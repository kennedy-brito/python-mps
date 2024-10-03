import json as j
class Reader():

  @staticmethod
  def readJson(name):
    with open(f"Aula-05-22/Exercicio 2/discoUtils/Json/{name}", "+r") as JF:
      parsedJson = j.load(JF)

    return parsedJson