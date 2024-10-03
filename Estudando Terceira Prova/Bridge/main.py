from formas import Circle, Square
from api_escrita import WriteConsole, WriteJson, WriteTxt

circuloConsole = Circle(4, WriteConsole())
circuloJson = Circle(3, WriteJson())
quadradoTxt = Square(5, WriteTxt())

circuloConsole.registrar_dados()
circuloJson.registrar_dados()
quadradoTxt.registrar_dados()
