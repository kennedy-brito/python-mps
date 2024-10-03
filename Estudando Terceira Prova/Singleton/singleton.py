from random import random
class Singleton:

  def __new__(cls) :
    
    if not hasattr(cls, "instance"):
      cls.instance = super(Singleton,cls).__new__(cls)
      cls.number = random() *1000

    return cls.instance
  
  def get_instance():
    return Singleton()
  

sg1 = Singleton()
sg2 = Singleton.get_instance()

print(f"sg1 is equal sg2? {sg1==sg2}")

print(sg1.number)
print(sg2.number)

