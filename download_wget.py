import wget
print('Beginning file download with wget module')

numero = "8- "
titulo = "Intro R - 4"
url = 'https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVJFMFhZRWFRU2N2U01FYkNzSHF5czhZQT09LS1jYmU0ZmZiOGIwMzExNGEzYTM0MDM1N2ZkNzU1MmFmYmNhYWMyOTNm.mp4'


extensao = ".mp4"
wget.download(url, "./videos/ESTATISTICA GERAL/" +  numero +  titulo + extensao )