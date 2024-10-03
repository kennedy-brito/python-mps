from .item import Item

class Consumivel(Item):

  def __init__(self,estragado = False, *args, **kwargs):
    self.estragado = estragado
    self._consumido = False
    super().__init__(*args, **kwargs)

  def comer(self):
    self._consumido = True
    self.usar()

  def usar(self):
    self.num_items -= 1
    print(f"o/a {self.nome} foi consumido(a)")
    if self.estragado:
      print("Essa não! Estava estragado!")
      print("o(a) personagem está passando mal.")

  @property
  def consumido(self):
    return self._consumido
  
  def __str__(self) -> str:
    return f"{self.nome} \t\t\t{self.num_items} \t\t{self.valor}G \t\t{self.peso}"

