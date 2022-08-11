from pytube import YouTube

url = input("Введите адрес: ")

yt = YouTube(url)
print(f'Загрузка видео: \n{yt.title!r}: {url}')

streams = yt.streams\
    .filter(progressive=True, file_extension='mp4', resolution='720p')\
    .order_by('resolution')

video = streams[-1]
# print('Stream url:', video.url)
video.download()
print('Видео успешно загружено!')
