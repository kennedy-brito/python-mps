class Writer():

  def __new__(self):
    
    if not hasattr(self, "instance"):
      self.instance = super(Writer, self).__new__(self)

    return self.instance
  
  def write(self, file, content):
    if not hasattr(self, "instance"):
      self.instance = super(Writer, self).__new__(self)
    print("escrevendo algo")
     
  def getInstance(self):
    if not hasattr(self, "instance"):
      self.instance = super(Writer, self).__new__(self)
