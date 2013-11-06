from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/videos/")
def videos():

    videos = mongo.db.test_data.find()

    str = ""
    for video in videos:
	print video
	for item in video:
	    str += "{item} : {value}\n".format(item=item, value=video[item])

    print str
    return str

@app.route("/")
def homepage():
    return "Talks Homepage!"

@app.route("/video/<int:video_id>")
def show_video(video_id):
    # gotta get video from database
    # then we can just display its attributes
    return "video {id}".format(id=video_id)

if __name__ == "__main__":
    app.name = "talks"
    app.debug = True
    app.run()
