from flask import Flask
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
	db.close()

@app.route("/videos/")
def videos():
    return "Videos Homepage!"

@app.route("/")
def homepage():
    return "Talks Homepage!"

@app.route("/video/<int:video_id>")
def show_video(video_id):
    # gotta get video from database

    # then we can just display its attributes
    return """ Video {id} by {author}
		{link} """.format(id=video_id)

def connect_db():
    c = MongoClient()

if __name__ == "__main__":
    app.debug = True
    app.run()
