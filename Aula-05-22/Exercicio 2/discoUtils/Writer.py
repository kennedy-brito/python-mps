import json as js
class Writer():

  @staticmethod
  def writeJson(parsingObject):
    
    name = f"{parsingObject.__class__()}_{parsingObject.id}"
    path = f"Aula-05-22/Exercicio 2/discoUtils/Json/{name}.json"
    print(name)
    print(path)
    with open(path,"w") as JF:
      JF.write(js.dumps(vars(parsingObject)))

