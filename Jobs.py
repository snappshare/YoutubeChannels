import Youtube
import os.path
import Branding
import ntpath


class BrandVideo:
    _Json = None  # type: Branding.Branding.Json

    def run(self):
        pass


class StealYoutubeVideo:
    class Json:
        Youtube_Uri = None
        Branding_Profile = None
        Downloaded_Path = None
        Branded_Path = None

    _Json = None  # type: Json

    def __init__(self, json: Json):
        self._Json = json

    def get_progress(self):
        total = 2
        done = 0
        if os.path.isfile(self._Json.Downloaded_Path):
            done = done + 1
        if os.path.isfile(self._Json.Branded_Path):
            done = done + 1
        return done / total

    def run(self):
        if not os.path.isfile(self._Json.Downloaded_Path):
            youtube = Youtube.Context()
            youtube.Download(
                self.Uri,
                os.path.dirname(self._Json.Downloaded_Path),
                ntpath.basename(self._Json.Downloaded_Path)
            )
        if not os.path.isfile(self._Json.Branded_Path):
            branding = Branding.Branding()
            branding.Run(self._Json.Branding_Profile)
            pass
