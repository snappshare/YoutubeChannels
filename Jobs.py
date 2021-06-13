import Youtube
import os.path
import ntpath

class BrandVideo:
    class Json:
        Intro_Start_End = None
        Outro_Start_End = None
        New_Intro_Start_End = None
        New_Outro_Start_End = None

    _Json = None

class StealYoutubeVideo:
    class Json:
        Youtube_Uri = None
        Branding_Profile = None
        Downloaded_Path = None
        Branded_Path = None

    _Json = None # type: Json

    def __init__(self, uri, branding_profile):
        self.Uri = uri
        self.Branding_Profile = branding_profile

    def get_progress(self):
        total = 2
        done = 0
        if os.path.isfile(self._Json.Downloaded_Path):
            done = done + 1
        if os.path.isfile(self._Json.Branded_Path):
            done = done + 1
        return done / total

    def run(self):
        youtube = Youtube.Context()
        if not os.path.isfile(self._Json.Downloaded_Path):
            youtube.Download(
                self.Uri,
                os.path.dirname(self._Json.Downloaded_Path),
                ntpath.basename(self._Json.Downloaded_Path)
            )
        if not os.path.isfile(self._Json.Branded_Path):
            pass
