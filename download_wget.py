import wget
print('Beginning file download with wget module')

numero = "9- "
titulo = "Ferramentas e práticas da Gestão 3.0 (parte 2)"
url = 'https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVNGMDR3RGFRUUJEMVlEYkNzSGd0MDRZQT09LS1iM2I1YjgyODQxMTE4NzQ5ZjM2NWFhYzgwZWU5MDYyMzU5YmZmOWU3.mp4'


extensao = ".mp4"
wget.download(url, "./videos/GERENCIAMENTO AGIL/Gerenciamento Ágil de Projetos/" +  numero +  titulo + extensao )