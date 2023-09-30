import pytube

url=input("linki giriniz: ")

path="C:\\Users\\tahak\\Desktop\\youtube video"

pytube.YouTube(url).streams.get_highest_resolution().download(path)


