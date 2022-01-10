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