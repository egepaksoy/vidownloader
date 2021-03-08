from flask import Flask, render_template
from video import video_info
app = Flask(__name__)

# TODO  video indirme uygulamasından kalıtım alcak
# TODO  sayfadan aldığı url'i name ile redirect yaparak başka linke aktarıcak


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/video/<string:url>")
def video(url):
    video = video_info(url)
    return render_template("video.html", video=video)


if __name__ == "__main__":
    app.run(debug=True)
