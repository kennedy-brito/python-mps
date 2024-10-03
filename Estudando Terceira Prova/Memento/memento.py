class Memento:

  def __init__(self, data) -> None:
    self.data = data

class Documento:

  def __init__(self) -> None:
    self.data = ""

  def write_text(self, text):
    self.data += text
  
  def save(self):
    return Memento(self.data)
  
  def undo(self, memento: Memento):
    self.data = memento.data

class TextEditor:

  def __init__(self) -> None:
    self.document = Documento()
    self._mementos = []

  def write(self, text):
    self.document.write_text(text)
  
  def save(self):
    self._mementos.append(self.document.save())

  def undo(self):
    if(len(self._mementos) == 0):
      return
    
    memento = self._mementos.pop()

    self.document.undo(memento)

  def __str__(self) -> str:
    return self.document.data
  
if __name__ == "__main__":
  txt = TextEditor()

  txt.save()
  txt.write("save1")
  txt.save()
  txt.write("\nsave2")

  print("========texto atual==========")
  print(txt)

  print("========texto 1 desfaz==========")
  txt.undo()
  print(txt)

  print("========texto 2 desfaz==========")
  txt.undo()
  print(txt)

  txt.undo()
  txt.undo()
  txt.undo()
  txt.undo()
  txt.undo()
  txt.undo()
  txt.undo()