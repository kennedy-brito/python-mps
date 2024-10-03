from .item import Item

class Arma(Item):

  TAXA_REDUCAO_DURABILIDADE = 0.05
  
  def __init__(self, dano_base:float, durabilidade_base: float, *args, **kwargs):
    self.dano_base = dano_base
    self._durabilidade_base = durabilidade_base
    super().__init__(*args, **kwargs)

  def usar(self):
    if self._durabilidade_base < 0:
      print("Sua arma não pode ser usada!")
      return
    
    self._durabilidade_base -= Arma.TAXA_REDUCAO_DURABILIDADE

    print(f"sua {self.nome} causou {self.dano_base} de dano!")
    
    if self._durabilidade_base < 0:
      print("Sua arma não pode ser usada!")
    

  def polir(self):
    aumento = 10* Arma.TAXA_REDUCAO_DURABILIDADE
    self._durabilidade_base += aumento
    print(f"Você poliu a {self.nome}! Sua nova durabilidade é {self.durabilidade}, até parece nova!")
    
  @property
  def durabilidade(self):
    return self._durabilidade_base
  
  def __str__(self) -> str:
    return f"{self.nome}({self.dano_base}A) \t\t\t{self.num_items} \t\t{self.valor}G \t\t{self.peso}"
