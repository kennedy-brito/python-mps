from memento import Memento
class Documento:

  def __init__(self) -> None:
    self.content = ''

  def write(self, texto):
    self.content += texto

  def save(self):
    return Memento(self.content)

  def undo(self, memento: Memento):
    self.content = memento.data

