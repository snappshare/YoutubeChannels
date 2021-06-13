import pyyoutube
import Jobs
import os

api = pyyoutube.Api(api_key='AIzaSyCPv-GvwuO6k-VlPuX_Ki8ZmGlDdaN-DlM')

#videos = api.search_by_keywords(q="lofi", search_type=["video"], count=5, limit=5)
#video = videos.items[0]
#url = "https://www.youtube.com/watch?v={}".format(video.id.videoId)
uri = 'https://www.youtube.com/watch?v=UZm8jB3wtQE'

my_path = os.path.abspath(os.path.dirname(__file__))
steal_json = Jobs.StealYoutubeVideo.Json()
steal_json.Downloaded_Path = my_path.join('/Videos/test.mp4')
steal_json.Branded_Path = my_path.join('/Videos/test_branded.mp4')
branding_json = Jobs.BrandVideo.Json()
branding_json.Intro_Start_End = [60, 60 + 25]
steal = Jobs.StealYoutubeVideo(steal_json)
steal.run()