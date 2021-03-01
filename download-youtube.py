import pytube
video_url = "https://www.youtube.com/watch?v=3kVvyWxerrI&feature=em-lbrm" 
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/pytube/Downloads') # vai gravar no C:\pytube\Downloads
