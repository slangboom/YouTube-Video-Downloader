from pytube import YouTube

# link = "https://www.youtube.com/watch?v=NpM7K-ygjxY" # my dad has a gtr
# link = "https://www.youtube.com/watch?v=4v0-dBoaKB8" # zoro
link = "https://www.youtube.com/watch?v=TWAPqCbPfiU"
my_video = YouTube(link)

print("*********************video title******************************")
print()
print(my_video.title)
print()

print("********************* pre reso ******************************")
my_video = my_video.streams.get_highest_resolution()

# video_quality = my_video.streams.all()
# video_quality = my_video.streams.filter()       # filter
# video_quality_list = list(enumerate(video_quality))

# for i in video_quality_list:
#     print(i)
  
# print()

# strm = int(input("enter: "))
print("*********************download initiated******************************")
# my_video[strm].download()

my_video.download()
print("*********************download successful******************************")
