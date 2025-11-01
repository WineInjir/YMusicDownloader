print("main.py started, initializing libraries...")

from yandex_music import Client 
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, APIC

with open("api.key") as f:
    key = f.read()

print("initializing yandex api")
client = Client(key).init()
print("yandex api initialized")

tracks = client.users_likes_tracks()
for i in range(0, len(tracks)):
    track = tracks[i].fetchTrack()
    title = track.title
    name = title.replace("/", "-")
    author = track.artists[0].name
    album = track.albums[0].title
    print(title, "by", author, "by album" , album)
    track.download("download/" + name + ".mp3", "mp3", 320)
    track.downloadCover("cover.jpg", '800x800')

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