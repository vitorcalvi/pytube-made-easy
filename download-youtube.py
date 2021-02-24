import pytube
video_url = "https://www.youtube.com/watch?v=4-079YIasck" 
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/pytube/Downloads') # vai gravar no C:\pytube\Downloads
