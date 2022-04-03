from flask import Flask, render_template
from data import users, userIdValues, default

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/profile/")
def profile():
    return render_template('profile.html')

@app.route("/feed/")
def feed():
    return render_template('feed.html')

@app.route("/messages/<int:value>")
def messages(value):
    user = userIdValues[value]
    return render_template('messages.html',user_data=user, default_response= default)

@app.route("/inbox/")
def inbox():
    return render_template('inbox.html', users=users)