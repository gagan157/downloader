from pytube import YouTube
from pytube import Playlist

# single video downloader
def ytdownload(urldata):
    save_path='D:/'
    yt = YouTube(urldata)
    title = yt.title
    tumbnail = yt.thumbnail_url
    vidviews= yt.views
    vidlenght = yt.length
    vidrating=yt.rating
    # st=yt.streams

    st = yt.streams.filter(res="720p",file_extension='mp4').get_by_itag(22)
    print("Downloading...")
    st.download(save_path)
    print(f"file name is {title} | Views {vidviews} | Duration {vidlenght} | Rating {vidrating}")
    print('Download Completed')



# Mutiyoutube download playlist
def mutiytdownloader(playlisturl):
    p=Playlist(playlisturl)
    save_path="D:/React js/"
    print(p.title)
    print(p.length)
    count=1
    for video in p.videos:
        # video.streams.first().download()
        video.title = f"{count}."+video.title
        print(f"Downloading....{video.title}")        
        extractvid=video.streams.filter(res="720p",file_extension='mp4').get_by_itag(22) 
        extractvid.download(save_path)
        count+=1
    print("Playlist Completed Download")


if __name__=='__main__':
    url="https://www.youtube.com/watch?v=-mJFZp84TIY&list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt&ab_channel=CodeWithHarry"
    # ytdownload(url)    
    # mutiytdownloader(url)