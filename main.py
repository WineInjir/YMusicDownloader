print("main.py started, initializing libraries...")

from yandex_music import Client 
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB

with open("api.key") as f:
    key = f.read()

print("initializing yandex api")
client = Client(key).init()
print("yandex api initialized")

tracks = client.users_likes_tracks()
for i in range(0, len(tracks)):
    track = tracks[i].fetchTrack()
    title = track.title
    author = track.artists[0].name
    album = track.albums[0].title
    print(title, "by", author, "by album" , album)
    track.download(title + ".mp3", "mp3", 192)
