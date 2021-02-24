import pytube
video_url = "https://nv.instructuremedia.com/fetch/QkFoYkIxc0hhUVFSbVQ4RWFRUXBRdWdEYkNzSGtoZzRZQT09LS03YzZhMzQwZDNjMTdjOGY0NDg5OGZhNTk1YTBmYmVmNzFkYjZmNjkw.mp4" 
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/pytube/Downloads') # vai gravar no C:\pytube\Downloads
