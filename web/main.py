from flask import Flask, render_template
from downloader import main as down

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/download/<video_inf>')
def download_page(video_inf):
    context = {
        "link": video_inf
    }
    return render_template("download.html", video=context)


@app.route('/indiriliyor/<kalite>')
def download(kalite):
