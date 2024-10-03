class FlyingMixIn:
  def fly(self):
    print("I'm flying!")


class Bird:
  def chirp(self):
    print("Chirp Chirp")

class Parrot(Bird,FlyingMixIn):
  pass

class Eagle(Bird, FlyingMixIn):
  pass

if __name__ == "__main__":
  parrot = Parrot()
  parrot.chirp()
  parrot.fly()

  eagle = Eagle()
  eagle.chirp()
  eagle.fly()
  