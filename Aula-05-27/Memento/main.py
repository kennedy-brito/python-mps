from documentoCaretaker import documentoCaretaker as doc

tcc = doc()
tcc.documento.write("teste 1")
tcc.save()
tcc.documento.write("teste 2")

print(tcc.documento.content)
tcc.undo()
print(tcc.documento.content)
