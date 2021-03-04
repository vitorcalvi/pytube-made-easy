from moviepy.editor import *
import os
from natsort import natsorted

L =[]

for root, dirs, files in os.walk('./video/ML/PT/Unidade 2 - Regras de associação/2- Algoritmos de regras de associação'):

    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile("./video/Youtube/Unidade 2.2- Algoritmos de regras de associação" + ".mp4",  remove_temp=False)