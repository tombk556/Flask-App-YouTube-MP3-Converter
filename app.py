import os
from flask import Flask, jsonify, request, render_template, send_file, redirect, url_for
from src.downloader import YouTubeMp3Downloader
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send', methods=["POST"])
def process():
    data=request.get_json()
    url=data.get('url') + "__"
    title=data.get('title') + "__"
    artist=data.get('artist') + "__"
    print(url, title, artist)
    response=jsonify({"url": url, "title":title, "artist": artist})
    
    return response

# @app.route('/home', methods=["GET", "POST"])
# def gfg():
#     if request.method == "POST":
#         url = request.form.get("url")
#         title = request.form.get("title")
#         artist = request.form.get("artist")
#         audio_file_name = f"{artist} - {title}"
#         print(audio_file_name)
#         print(url)

#     return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
