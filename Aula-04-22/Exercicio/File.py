from typing import List

class File:
  def __init__(self, file_name:str, root_path:str) -> None:
    self.file_name = file_name
    self.root_path = root_path

  def open(self):
    pass

  def close(self):
    pass

  def check_integrity(self, hash_value):
    pass


class FileReader(File):
  def __init__(self, *args) -> None:
    super().__init__(*args)

  def read_line():
    pass

  def read_all():
    pass


class FileWriter(File):
  def __init__(self, *args) -> None:
    super().__init__(*args)

  def write(self, content):
    pass

  def append(self, content):
    pass