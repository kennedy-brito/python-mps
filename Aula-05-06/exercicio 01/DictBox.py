from Box import Box
class DictBox(Box):

  def __init__(self):
    self._items = {}

  @property
  def items(self):
    return self._items
  
  def add(self, items: dict):
    self._items.update(items)


  def esvaziar(self):
    self._items = {}
    

  def contar(self):
    return len(self._items)
