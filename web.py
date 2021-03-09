from flask import Flask, render_template, request, redirect, send_file
from video import video_info, video_download
import os
app = Flask(__name__)

# TODO  video indirme uygulamasından kalıtım alcak
# TODO  sayfadan aldığı url'i name ile redirect yaparak başka linke aktarıcak


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/video", methods=['GET', 'POST'])
def video():
    if request.method == "POST":
        url = request.form.get("videourl")
        yt = video_info(url)
        return render_template("yt_video.html", yt=yt)
    else:
        return render_template("yt_video.html")


@app.route("/download/<string:url>/<int:sira>")
def download(url, sira):
    url = "https://youtube.com/watch?v="+url
    video_download(url, sira)
    path = "/home/ege/Downloads/vidownload/"+video_info(url)[0].title+"mp4"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
