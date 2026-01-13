print("main.py started, initializing libraries...")

import configparser
import time
from yandex_music import Client 
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, APIC
import telebot

config = configparser.ConfigParser()
config.read("config.ini")
key = config["Yandex"]["key"]

token = config["Telegram"]["token"]

print("initializing yandex api")
client = Client(key).init()
print("yandex api initialized")

tracks = client.users_likes_tracks()
for i in range(0, len(tracks)):
    
    succes = False
    while succes != True:
        try:
            track = tracks[i].fetchTrack()
            time.sleep(0.5)

            succes = True
            break
        except:
            succes = False
            time.sleep(5)

    title = track.title
    name = title.replace("/", "-")
    author = track.artists[0].name
    album = track.albums[0].title

    info = track.get_download_info()
    time.sleep(0.5)

    qlist = list()
    tmp = 0
    for i in range(len(info)):
        qlist.append(info[i].bitrate_in_kbps)
    quality = int(max(qlist))

    succes = False
    while succes != True:
        try:
            track.download("download/" + name + ".mp3", "mp3",  quality)
            time.sleep(0.5)

            track.downloadCover("cover.jpg", '800x800')
            time.sleep(0.5)

            succes = True
            break
        except:
            succes = False
            time.sleep(5)


    tags = ID3()
    tags["TIT2"] = TIT2(encoding=3, text=[title])
    tags["TPE1"] = TPE1(encoding=3, text=[author])
    tags["TALB"] = TALB(encoding=3, text=[album])
    with open("cover.jpg", "rb") as f:
        tags["APIC"] = APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc='Cover',
            data=f.read()
       )
    tags.save("download/" + name + ".mp3")
    
    print("Downloaded",title, "by", author, "by album" , album, "quality:", quality)