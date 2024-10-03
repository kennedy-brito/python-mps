from documento import Documento
class documentoCaretaker:

  def __init__(self) -> None:
    self.mementos = []
    self.documento = Documento()

  def save(self):
    self.mementos.append(self.documento.save())

  def undo(self):
    if not len(self.mementos):
      return None
    memento = self.mementos.pop()

    self.documento.undo(memento)

