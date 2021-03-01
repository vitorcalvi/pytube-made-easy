import wget
print('Beginning file download with wget module')

numero = "2- "
titulo = "Videoaula - Regras de Associação suporte e confiança"
url = 'https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVRJOG9RRGFRU0QvMUFEYkNzSDdZcytZQT09LS1jZTQwNjlhOWQxNTJhZGYxYjIzZmM3ZjM4YjYzOGExYzM2ZDE5MjY1.mp4'


extensao = ".mp4"
wget.download(url, "./video/Machine Learning/Princípios e técnicas de aprendizado de máquina/Unidade 2 - Regras de associação/1- Conjuntos de itens frequentes, suporte e confiança/" +  numero +  titulo + extensao )