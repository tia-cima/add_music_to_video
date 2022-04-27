import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Start: ", current_time)

videoIndex = 1
audioIndex = 1
nvideo = 0
nsong = 0
resolution = (480,848)
path_music = "music/"
path_video = "video/"
path_new = "NEW_VIDEO/"
path_temp = "temp_video/"

while(videoIndex <= nvideo):    
    if(audioIndex >= nsong + 1):
        audioIndex = 1
    print("\n\nVideo number: " + str(videoIndex) + "\tSong number: " + str(audioIndex))
    video = mp.VideoFileClip(path_video + "video (" + str(videoIndex) + ").mp4")
    end_time = video.duration
    audio = mp.AudioFileClip(path_music + "song (" + str(audioIndex) + ").mp3")
    video = video.set_audio(audio)
    print(str(video.rotation))
    if(video.rotation == 0): # if the video is vertical this if maintains the resolution
        print("Horizontal video, won't change the resolution")
        video.write_videofile(path_temp + "temp_video" + str(videoIndex) + ".mp4")
    else:
        print("Vertical video, will change the resolution")
        video.resize(resolution).write_videofile(path_temp + "temp_video" + str(videoIndex) + ".mp4")
    videoNew = ffmpeg_extract_subclip(path_temp + "temp_video" + str(videoIndex) +".mp4", 0, end_time, targetname=path_new + "new_video" + str(videoIndex) + ".mp4")
    videoIndex += 1
    audioIndex += 1

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("End: ", current_time)