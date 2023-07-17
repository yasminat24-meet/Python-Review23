def create_youtube_video (title, description):
	youtubevideo= {"title":title ,"description": description, "likes": 0,"dislikes": 0, "comments":{ }}
	return  youtubevideo
def like(video):
	if like in video:
		video["likes"]+=1
	return video
def dislike(video):
	if dislike in video:
		video["dislikes"]+=1
	return video
def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"]["username"]=comment_text
	return youtubevideo
yv=create_youtube_video("cake","how to make cake")
print(yv)
like(yv)
dislike(yv)
add_comment(yv,"jazz","sushi is amazing")
print(yv)
for i in range (495):
	like(yv)
print(yv)


