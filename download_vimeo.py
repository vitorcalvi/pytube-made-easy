import vimeo_dl as vimeo
url = "https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVFSbVQ4RWFRUXBRdWdEYkNzSGtoZzRZQT09LS03YzZhMzQwZDNjMTdjOGY0NDg5OGZhNTk1YTBmYmVmNzFkYjZmNjkw.mp4"
video = vimeo.new(url)

video.download(quiet=False)