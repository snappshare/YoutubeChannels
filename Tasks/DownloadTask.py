class DownloadTask:
    Uri = None
    Path = None

    def __init_(self, uri, path):
        self.Uri = uri
        self.Path = path

    def run(self, context):
        context.Download(self.Uri, self.Path)
        return True
