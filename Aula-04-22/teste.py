def teste2(*args):
  print(args)

def teste(**kwargs):
  teste2(kwargs)



teste(a=1,b=2,c=3,d=4,e=5,f=6,g=7)