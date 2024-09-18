# from pytube import YouTube
from pytube import YouTube

link = input("please provide your link")
check = input("what do you want to download press 1 for video press 2 for audio ")


if check == "1":
    youtube_1 = YouTube(link)
    videos = youtube_1.stream.filter(progressive = True)
    for i,v in enumerate(videos):
        print(i,v)
    strm = int(input("please provide your index you want to download"))
    videos[strm].download()
    print("successfully done")