import wget
print('Beginning file download with wget module')

url = 'https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVFSbVQ4RWFRUXBRdWdEYkNzSGtoZzRZQT09LS03YzZhMzQwZDNjMTdjOGY0NDg5OGZhNTk1YTBmYmVmNzFkYjZmNjkw.mp4'
arquivo = "Arquitetura De Um Sistema Web.mp4"
wget.download(url, "./videos/FRAMEWORKS BACK END – JAVA, .NET E PHP/" + arquivo)