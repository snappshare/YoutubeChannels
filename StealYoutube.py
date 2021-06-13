class StealYoutube:
    Uri = None
    Branding_Profile = None
    Downloaded_Path = None
    Branded_Path = None
    #Uploaded_Path = None

    def __init__(self, uri, branding_profile):
        self.Uri = uri
        self.Branding_Profile = branding_profile

    def get_progress(self):
        total = 2
        done = 0
        if self.Downloaded_Path is not None:
            done = done + 1
        if self.Branded_Path is not None:
            done = done + 1
        return done / total

    def run(self):
        context = Context
        if self.Downloaded_Path is None:

