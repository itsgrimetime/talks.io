from flask import Flask, url_for, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/videos/")
def videos():

    videos = mongo.db.test_data.find()
    return render_template('videos.htmljinja', videos=videos)

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
