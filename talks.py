from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Talks Homepage!"

@app.route("/video/<int:video_id>")
def show_video(video_id):
    return "Video %d" % video_id

if __name__ == "__main__":
    app.run()
