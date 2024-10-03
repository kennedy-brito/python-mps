from Box import Box 
class ListBox(Box):

  def __init__(self):
    self._items = []

  def add(self, items: list):
    self._items += items

  @property
  def items(self):
    return self._items

  def esvaziar(self):
    self._items = []

  def contar(self):
    return len(self._items)
