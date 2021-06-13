import Youtube
import os.path
import ntpath
import Json


class StealYoutubeVideo:
    _Json = None  # type: Json.StealYoutubeVideoJson

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
                self._Json.Youtube_Uri,
                os.path.dirname(self._Json.Downloaded_Path),
                ntpath.basename(self._Json.Downloaded_Path)
            )
        if not os.path.isfile(self._Json.Branded_Path):
            branding = Branding.Branding()
            branding.Run(self._Json.Branding_Profile)
            pass
