from abc import ABC, abstractmethod
class Chair:

  def __init__(self) -> None:
    self.movel = ''
    pass

class Sofa:

  def __init__(self) -> None:
    self.movel = ''
    pass


class CoffeeTable:

  def __init__(self) -> None:
    self.movel = ''
    pass

class VictorianChair(Chair):

  def __init__(self) -> None:
    self.movel = "cadeira vitoriana"

class ArtDecoChair(Chair):

  def __init__(self) -> None:
    self.movel = "cadeira de arte Deco"

class ModernChair(Chair):

  def __init__(self) -> None:
    self.movel = "cadeira moderna"

class VictorianSofa(Sofa):

  def __init__(self) -> None:
    self.movel = "sofa vitoriana"

class ArtDecoSofa(Sofa):

  def __init__(self) -> None:
    self.movel = "sofa de arte Deco"

class ModernSofa(Sofa):

  def __init__(self) -> None:
    self.movel = "sofa moderna"

class VictorianCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.movel = "mesa de café vitoriana"

class ArtDecoCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.movel = "mesa de café de arte Deco"

class ModernCoffeeTable(CoffeeTable):

  def __init__(self) -> None:
    self.movel = "mesa de café moderna"