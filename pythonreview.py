def create_youtube_video (title, description):
	youtubevideo= {"title":title ,"description": description, "likes": 0,"dislikes": 0, "comments":{ "username":username}}
	return  youtubevideo
def like(video):
	if likes in video:
		video["likes"]+=1
	return youtube_video_dictionary
def dislike(video):
	if dislikes in video:
		video["dislikes"]+=1
def add_comment(youtubevideo, username, comment_text):
	video["comment"]["username"]=comment_text
	return video
yv=  Create_youtube_video("cake","sushi")
print(yv)
likes(yv)
dislikes(yv)
add_comment(yv,"jazz","sushi is amazing")
print(yv)
for i in (495):
	like(yv)
print(yv)


