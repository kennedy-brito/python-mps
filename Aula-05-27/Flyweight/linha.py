class PontoFlyweight():
  
  def __init__(self, x, y) -> None:
    self.x = x 
    self.y = y

class Linha:

  pontos = {}
  colors = {}

  def __init__(self, x1, y1, x2, y2):

    p = "-".join(x1,y1)
    
    if p not in Linha.pontos:
      Linha.pontos[p] = PontoFlyweight(x1, y1)
    
    self.p1 = Linha.pontos[p]

    p = "-".join(x2,y2)
    if p not in Linha.pontos:
      Linha.pontos[p] = PontoFlyweight(x2, y2)
    self.p2 = Linha.pontos[p]
