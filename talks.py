import video

from flask import Flask, url_for, render_template, redirect
from flask.ext.pymongo import PyMongo

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def homepage():
    return render_template('main.htmljinja')

####### Videos #########

@app.route("/videos/")
def videos():

    videos = mongo.db.test_data.find()
    return render_template('videos.htmljinja', videos=videos)

@app.route("/video/<int:video_id>")
def show_video(video_id):
    # gotta get video from database
    # then we can just display its attributes
    return "video {id}".format(id=video_id)

@app.route("/submit", methods =('GET', 'POST'))
def submit():
    form = SubmitForm(csrf_enabled = False)
    if form.validate_on_submit():
	vid = video.Video()
	vid.title = form.title.data
	vid.link = form.link.data
	vid.submitter = form.submitter.data
	vid.author = form.author.data
	mongo.db.test_data.insert(vid.__dict__)
	return redirect(url_for('videos'))
    else:
	return render_template('submit.htmljinja', form=form)

class SubmitForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    link = TextField('Link', validators=[DataRequired()])
    submitter = TextField('Submitter', validators=[DataRequired()])
    author = TextField('Author', validators=[DataRequired()])

if __name__ == "__main__":
    app.name = "talks"
    app.debug = True
    app.run()
