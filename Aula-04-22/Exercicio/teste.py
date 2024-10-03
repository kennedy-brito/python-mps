from Directory import Directory

novoDiretorio = Directory("/");

novoDiretorio.create_directory("subpasta")
novoDiretorio.create_file("foto")

print(novoDiretorio.sub_directories)
print(novoDiretorio.file_open)
novoDiretorio.open_file('foto', 'r');
print(novoDiretorio.file_open.root_path)
