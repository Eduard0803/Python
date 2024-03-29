import os
import re

import moviepy.editor as mp
from pytube import YouTube

link = input("Digite o link do video: ")
path = input("Digite o caminho para salvar o arquivo: ")

char = '"'
for i in char:
    path = path.replace(i, "")

yt = YouTube(link)

print("Download...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download Completo!")

print("Convertendo Arquivo")
for file in os.listdir(path):
    if re.search("mp4", file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp3")
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucesso!")
