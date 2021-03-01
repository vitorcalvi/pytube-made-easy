#pip install moviepy

from moviepy.editor import VideoFileClip, concatenate_videoclips
video_1 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/1- Papéis Scrum Master.mp4")
video_2 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/2- Papéis Product Owner.mp4")

video_3 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/3- Papéis Development Team.mp4")
video_4 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/4- Artefatos.mp4")
video_5 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/5- Outros Artefatos.mp4")
video_6 = VideoFileClip("./videos/GERENCIAMENTO AGIL/Framework Scrum/6- Eventos.mp4")
final_video= concatenate_videoclips([video_1, video_2,video_3, video_4,video_5, video_6])
final_video.write_videofile("./videos/GERENCIAMENTO AGIL/Framework Scrum/final_video.mp4")