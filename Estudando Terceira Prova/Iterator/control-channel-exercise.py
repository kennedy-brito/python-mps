from collections import abc
class Program():

  def __init__(self, time: int, duration: int) -> None:
    self.time = time
    self.duration = duration
  
  def __str__(self) -> str:
    horario = str(self.time)+":00" + ("PM" if self.time>=12 else "AM")
    fim = str(self.time + self.duration)+":00" + ("PM" if self.time + self.duration >=12 else "AM")
    return f"start at {horario} ends {fim}"

class Channel:

  def __init__(self, frequency) -> None:
    self.frequency = frequency
    self._programs = []

  def add_program(self, program: Program):
    self._programs.append(program)

  def __iter__(self):
    return ProgramIterator(self._programs)

class Tv:

  def __init__(self) -> None:
    self._channels = []
  
  def add_channel(self, channel: Channel):
    self._channels.append(channel)

  def __iter__(self):
    return RemoteController(self._channels)
  
  def find_programs_start(self, start: int):
    programs = []
    for channel in self:
      for program in channel:

        if program.time == start:
          programs.append(program)

    return programs 

class ProgramIterator():

  def __init__(self, programs) -> None:
    self._programs = programs
    self._index = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if(self._index>= len(self._programs)):
      raise StopIteration
    
    program = self._programs[self._index]
    self._index+=1

    return program
  
  def __previous__(self):
    if(self._index < 0):
      raise StopIteration
    
    program = self._programs[self._index]
    self._index-=1

    return program
  
class RemoteController():

  def __init__(self, channels) -> None:
    self._channels = channels
    self._index = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if(self._index>= len(self._channels)):
      raise StopIteration
    
    program = self._channels[self._index]
    self._index+=1

    return program
  
  def __previous__(self):
    if(self._index < 0):
      raise StopIteration
    
    program = self._channels[self._index]
    self._index-=1

    return program



if __name__ == "__main__":

  channel1 = Channel("0001")

  channel1.add_program(Program(12,2))
  channel1.add_program(Program(9,2))
  
  channel2 = Channel("0002")

  channel2.add_program(Program(13,2))
  channel2.add_program(Program(21,2))

  tv1 = Tv()
  tv1.add_channel(channel1)
  tv1.add_channel(channel2)

  for program in tv1.find_programs_start(12):
    print(program)
