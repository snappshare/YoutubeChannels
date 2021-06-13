import pyyoutube
import Jobs
import os
import Json

api = pyyoutube.Api(api_key='AIzaSyCPv-GvwuO6k-VlPuX_Ki8ZmGlDdaN-DlM')

#videos = api.search_by_keywords(q="lofi", search_type=["video"], count=5, limit=5)
#video = videos.items[0]
#url = "https://www.youtube.com/watch?v={}".format(video.id.videoId)

my_path = os.path.abspath(os.path.dirname(__file__))
steal_json = Json.StealYoutubeVideoJson()
steal_json.Youtube_Uri = 'https://www.youtube.com/watch?v=UZm8jB3wtQE'
steal_json.Downloaded_Path = os.path.join(my_path, 'Videos/test')
steal_json.Branded_Path = os.path.join(my_path, 'Videos/test_branded')
branding_json = Json.BrandingJson()
branding_json.Intro_Start_End = [60, 60 + 25]
steal = Jobs.StealYoutubeVideo(steal_json)
steal.run()
