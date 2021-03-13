from pytube import YouTube

url = input("Paste the url of any YouTube video here\n")
video = YouTube(url)

print("Downloading...")
video.streams.get_highest_resolution().download("Video")
print("Video downloaded.")