class BrandingProfile:
    Intro_Start_End = None
    Outro_Start_End = None
    Intro_Path = None
    Outro_Path = None

    def __init__(self, intro_start_end = None, outro_start_end = None, intro_path = None, outro_path = None):
        self.Intro_Start_End = intro_start_end
        self.Outro_Start_End = outro_start_end
        self.Intro_Path = intro_path
        self.Outro_Path = outro_path