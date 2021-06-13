import pyyoutube
from Classes.Context import Context


api = pyyoutube.Api(api_key='AIzaSyCPv-GvwuO6k-VlPuX_Ki8ZmGlDdaN-DlM')

#videos = api.search_by_keywords(q="lofi", search_type=["video"], count=5, limit=5)
#video = videos.items[0]
#url = "https://www.youtube.com/watch?v={}".format(video.id.videoId)
uri = "https://www.youtube.com/watch?v=UZm8jB3wtQE"

context = Context()
context.Download(uri, "Youtube", "test")