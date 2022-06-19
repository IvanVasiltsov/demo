import textwrap
import youtube_dl
import json
from functools import reduce
import math as mt
""" Программа подсчитывает длительность всех видео в плейлисте"""

url = 'https://youtube.com/playlist?list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E'  # сохраненный плейлист
ydl_opts = {"extract_flat": True}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    playlist = ydl.extract_info(url=url, download=False, extra_info=ydl)
    playlist_dict_entries = playlist['entries']

    newList = []
    for item in playlist_dict_entries:
        duration = item['duration']  # доступ к значению словаря по ключу : duration
        newList.append(int(duration))

    print(newList)  # длительность видео в сек. каждого видео в плейлисте
    time_all = reduce(lambda x, y: x+y, newList)
    print(f"Время в секундах плейлиста : {time_all} , время в минутах : {time_all/60}, "
          f"время в часах: {mt.ceil(time_all/3600)}")


