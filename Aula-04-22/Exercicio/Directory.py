from typing import List
from File import FileReader, FileWriter

class Directory(FileReader, FileWriter):
  def __init__(self, path:str) -> None:
    self.path = path
    self.file_list = []
    self.file_open = None
    self.sub_directories = []


  def delete_directory(self, directory_name):
    self.sub_directories.remove(directory_name)

  def create_directory(self, directory_name):
    self.sub_directories.append(directory_name)

  def rename_directory(self, old_name, new_name):
    sub_directory_index = self.sub_directories.index(old_name)
    self.sub_directories[sub_directory_index] = new_name


  def delete_file(self, file_name):
    self.file_list.remove(file_name)

  def create_file(self, file_name):
    self.file_list.append(file_name)

  def rename_file(self, old_name, new_name):
    file_index = self.file_list.index(old_name)
    self.file_list[file_index] = new_name

  def open_file(self, name_file, mode:str):
    if name_file in self.file_list:
      if mode == 'r':
        self.file_open = FileReader(name_file, self.path)
      elif mode == 'w':
        self.file_open = FileWriter(name_file, self.path)
      else:
        print("modo não suportado")

      return

    print("arquivo não existe");  
