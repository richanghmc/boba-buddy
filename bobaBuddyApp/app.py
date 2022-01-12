from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route("/profile/")
def login():
    return render_template('profile.html')

@app.route("/feed/")
def feed():
    return render_template('feed.html')

@app.route("/messages/")
def messages():
    return render_template('messages.html')

@app.route("/inbox/")
def inbox():
    return render_template('inbox.html')