from pytube import YouTube

class Context:
    def Download(self, uri, path, filename):
        video = YouTube(uri).streams.get_highest_resolution()
        video.download(path, filename, max_retries=10)